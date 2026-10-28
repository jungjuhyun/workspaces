#!/usr/bin/env python3
"""Validate the document workflow using file inputs only.
No network, model calls, music generation or audio playback.
All case records are TEST_ONLY and never enter the real research ledger.
"""
import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path

VERSION = "0.19.1"
CORE = [
 "00_START_HERE.md","01_RESEARCH_PLAN.md","02_PRODUCTION_STANDARD.md",
 "03_EVIDENCE_REGISTER.md","04_PRODUCTION_HISTORY.md",
 "05_DECISIONS_AND_PROGRESS.md","06_SELECTION_CRITERIA.md",
 "07_REVIEW_REPORT.md","08_REDTEAM_REPORT.md","project_state.json"
]
REQUIRED_PHASES = ["P1","P2_SCOPE","P3","P4","P5","P6","P7"]

def sha(value):
    if isinstance(value,str): value=value.encode("utf-8")
    return hashlib.sha256(value).hexdigest()

def rows(text, pattern):
    return [line for line in text.splitlines() if re.match(pattern,line)]

def owned_row(text, code):
    found=rows(text,r"^\| "+code+r" \|")
    if not found: raise ValueError("Missing owner row "+code)
    return [part.strip() for part in found[0].split("|")[1:-1]]

def test_ids(text):
    result=set()
    for first,last,single in re.findall(r"T(\d{2})~T(\d{2})|T(\d{2})",text):
        if single: result.add("T"+single)
        else:
            result.update("T%02d"%n for n in range(int(first),int(last)+1))
    return result

def decision_scope(docs):
    rules=docs["06_SELECTION_CRITERIA.md"]
    d05=owned_row(rules,"D05")[2].split(". T06")[0]
    d07=owned_row(rules,"D07")[2]
    return test_ids(d05), set(re.findall(r"D\d{2}",d07))

def cycle_path(graph):
    active=[];done=set()
    def visit(node):
        if node in active:return active[active.index(node):]+[node]
        if node in done:return None
        active.append(node)
        for dep in graph[node]:
            if dep not in graph:return [node,"UNKNOWN:"+dep]
            found=visit(dep)
            if found:return found
        active.pop();done.add(node)
        return None
    for node in graph:
        found=visit(node)
        if found:return found
    return []

def inspect(docs,state,fixtures,baseline,root,publication=False):
    checks=[]
    def add(name,ok,detail):
        checks.append({"id":name,"passed":bool(ok),"detail":detail})
    production=docs["02_PRODUCTION_STANDARD.md"]
    criteria=docs["06_SELECTION_CRITERIA.md"]
    rrows=rows(production,r"^\| R\d{2} \|")
    rids=[owned.split("|")[1].strip() for owned in rrows]
    add("A1.requirements",sha("\n".join(rrows))==baseline["requirements_sha256"]
        and len(rids)==len(set(rids))==22
        and set(rids)=={"R%02d"%n for n in range(1,23)},
        "Requirement/source/condition rows retained against the pre-edit baseline")
    add("A1.T",sha("\n".join(rows(criteria,r"^\| T\d{2} \|")))==baseline["T_sha256"],
        "All eight sound-observation rows retained")
    add("A1.G",sha("\n".join(rows(criteria,r"^\| G\d{2} ")))==baseline["G_sha256"],
        "All ten plan-acceptance rows retained")
    add("A1.frozen_cases",sha((root/"workflow_cases.json").read_bytes())==baseline["cases_sha256"],
        "Acceptance inputs and expected outcomes were not weakened")
    music=production.split("## 부록 A.")[0]
    u_music=set(re.findall(r"^\| (U\d{2}) \|",music,re.M))
    u_ops=set(re.findall(r"^\| (U\d{2}) \|",
        production.split("## 부록 B.")[1].split("## 부록 C.")[0],re.M))
    add("A2.roles",u_music=={"U01","U02","U03","U04","U05","U11"}
        and u_ops=={"U06","U07","U08","U09","U10"},
        "Music and operational U items have distinct owners")
    required,preset_deps=decision_scope(docs)
    add("A3.single_track_scope",required=={"T01","T02","T03","T04","T05","T07","T08"},
        "D05 excludes cross-track T06 but retains keyboard observation")
    add("A3.preset_dependencies",{"D04","D05"}.issubset(preset_deps),
        "A selected track alone cannot validate the default preset")
    graph=state["workflow"]["phase_dependencies"]
    cycle=cycle_path(graph)
    add("A3.acyclic",not cycle,"Dependency cycle: "+repr(cycle))
    add("A3.dependency_contract",set(graph)==set(REQUIRED_PHASES)
        and graph==fixtures["phase_dependencies"],
        "Scope-review events are separated from effect-claim validation")
    impact=state["workflow"]["impact_review"]
    by_file={item["file"]:item for item in impact}
    add("A6.impact_coverage",set(by_file)==set(CORE)
        and all(x["disposition"] in {"modified","unchanged"} and x["reason"] for x in impact),
        "Every original file has a modification or an explained no-impact disposition")
    mismatch=[]
    for name,entry in by_file.items():
        changed=sha((root/name).read_bytes())!=baseline["file_hashes"][name]
        if changed != (entry["disposition"]=="modified"):mismatch.append(name)
    add("A6.actual_change_impact",not mismatch,"Disposition/content mismatch: "+repr(mismatch))
    needed={"00_START_HERE.md","01_RESEARCH_PLAN.md","05_DECISIONS_AND_PROGRESS.md",
            "06_SELECTION_CRITERIA.md","07_REVIEW_REPORT.md","project_state.json"}
    add("A6.owner_consumers",all(by_file.get(n,{}).get("disposition")=="modified" for n in needed),
        "Procedure owner change covers entry, plan, progress, report and state consumers")
    for name,text in docs.items():
        refs=set(re.findall(r"\b\d{2}_[A-Z_]+\.md\b",text))
        add("A2.refs."+name,all((root/ref).is_file() for ref in refs),
            "Referenced document files resolve")
    registered=set(re.findall(r"^### (SRC-\d{4})",docs["03_EVIDENCE_REGISTER.md"],re.M))
    external=state.get("external_source_ids",[])
    add("A7.actual_scope",state["external_sources_count"]==len(external)
        and len(set(external))==len(external) and set(external).issubset(registered)
        and state["direct_audio_checks_count"]==0 and state["generation_attempts_count"]==0,
        "Declared external method sources match actual records; no direct listening or generation")
    if publication:
        expected=set(CORE+["workflow_cases.json","workflow_validator.py","workflow_validation.json","09_ORIGINAL_ANALYSIS.md","10_PRODUCT_CAPABILITIES.md","11_CASE_RESEARCH.md","12_MUSICAL_OPTIONS.md","13_EVIDENCE_AND_TEST_PLAN.md","14_REQUEST_INTAKE.md","15_REPEATABLE_PRODUCTION_WORKFLOW.md","p5_workflow_cases.json","16_FIRST_BATCH_DESIGNS.md","first_batch_designs.json","17_TRACK01_INPUT.md","18_PROMPT_REGISTER.md"])
        refs=state["authoritative_file_refs"]
        mapping={x["name"]:x["library_file_id"] for x in refs}
        add("A8.canonical_files",set(mapping)==expected
            and len(set(mapping.values()))==len(expected)
            and all(re.fullmatch(r"libfile_[0-9a-f]+",v) for v in mapping.values()),
            "Every deliverable is pinned to its actual saved Library identity")
    return checks

def execute_case(case,docs,state):
    data=copy.deepcopy(case["input"])
    required,preset_deps=decision_scope(docs)
    allowed=set(data.get("authorized",[]))
    completed=set(data.get("events",[]))
    graph=state["workflow"]["phase_dependencies"]
    if data.get("request")=="stop":
        next_task="STOPPED"
    elif "research" not in allowed:
        next_task="DOCUMENT_REVIEW"
    elif not data.get("baseline_attempted",False):
        next_task="BASELINE_LOOKUP"
    else:
        next_task="NO_READY_TASK"
        for phase,deps in graph.items():
            if phase not in completed and set(deps).issubset(completed):
                next_task=phase;break
        if next_task=="P7" and "generation" not in allowed:
            next_task="WAIT_GENERATION_SCOPE"
    observed=set(data.get("observed_tests",[]))
    audio=("PASS_OBSERVED_SCOPE" if data.get("has_reference")
        and data.get("fixture_direct_observation") and required.issubset(observed)
        else "UNASSESSED")
    adoption="USER_SELECTED" if data.get("user_selected") else "NOT_SELECTED"
    actual_effect=bool(data.get("repeat_validation",False))
    evidence={"D04":actual_effect,"D05":audio=="PASS_OBSERVED_SCOPE"}
    preset=("VALIDATED_OBSERVED_SCOPE" if all(evidence.get(d,False) for d in preset_deps)
        and adoption=="USER_SELECTED" else "UNVALIDATED")
    candidate=None
    if data.get("option_supported") and data.get("experiment_plan"):
        candidate="CASE_SUPPORTED" if data.get("public_case") else "EXPLORATORY"
    diversity="NOT_ASSESSED"
    if "design_a" in data and "design_b" in data:
        features=("motif","groove","harmony","interaction","intro")
        diversity=("REVISE" if all(data["design_a"].get(k)==data["design_b"].get(k)
            for k in features) else "DISTINCTION_DOCUMENTED_ONLY")
    blocked=[] if data.get("has_reference") else ["D05","D07"]
    return {
        "next":next_task,
        "can_generate":next_task=="P7" and "generation" in allowed,
        "blocked":blocked,"effect_claim":data.get("effect_claim","UNRESOLVED"),
        "audio":audio,
        "long_listening":"PASS_REPORTED_SCOPE" if data.get("full_length_observed") else "UNASSESSED",
        "adoption":adoption,"preset":preset,"candidate_kind":candidate,
        "validated_effect":actual_effect,
        "source_effect":"OBSERVED_SCOPE_ONLY" if actual_effect else "NOT_ESTABLISHED",
        "diversity":diversity
    }

def case_results(cases,docs,state,out=None):
    results=[]
    for case in cases:
        actual=execute_case(case,docs,state)
        failures={k:{"expected":v,"actual":actual.get(k)}
            for k,v in case["expected"].items() if actual.get(k)!=v}
        record={
            "test_only":True,"not_real_music_research_or_audio":True,
            "case_id":case["id"],"input":case["input"],
            "expected":case["expected"],"actual":actual,"passed":not failures,
            "failures":failures,
            "action_record":{"next_task":actual["next"],"actual_external_action_performed":False},
            "scope_note":"Hypothetical evidence flags exercise document routing; no real audio was heard."
        }
        if out:
            (out/(case["id"]+".json")).write_text(
                json.dumps(record,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        results.append(record)
    return results

def mutations(docs,state,fixtures,baseline,root):
    results=[]
    for name in ["M01_R22_omission","M02_D05_requires_T06",
                 "M03_phase_cycle","M04_preset_lacks_D04"]:
        md=copy.deepcopy(docs);st=copy.deepcopy(state)
        if name=="M01_R22_omission":
            md["02_PRODUCTION_STANDARD.md"]="\n".join(
                l for l in md["02_PRODUCTION_STANDARD.md"].splitlines()
                if not l.startswith("| R22 |"))
        elif name=="M02_D05_requires_T06":
            lines=md["06_SELECTION_CRITERIA.md"].splitlines()
            index=next(i for i,l in enumerate(lines) if l.startswith("| D05 |"))
            assert "T01~T05·T07" in lines[index]
            lines[index]=lines[index].replace("T01~T05·T07","T01~T08")
            md["06_SELECTION_CRITERIA.md"]="\n".join(lines)
        elif name=="M03_phase_cycle":
            st["workflow"]["phase_dependencies"]["P2_SCOPE"].append("P7")
        else:
            lines=md["06_SELECTION_CRITERIA.md"].splitlines()
            index=next(i for i,l in enumerate(lines) if l.startswith("| D07 |"))
            assert "D04·D05" in lines[index]
            lines[index]=lines[index].replace("D04·D05","D05")
            md["06_SELECTION_CRITERIA.md"]="\n".join(lines)
        checks=inspect(md,st,fixtures,baseline,root)
        behavioral=[]
        if name!="M03_phase_cycle":
            behavioral=[x["case_id"] for x in case_results(fixtures["cases"],md,st) if not x["passed"]]
        detected=[x["id"] for x in checks if not x["passed"]]
        results.append({"mutation":name,"test_only":True,
            "rejected":bool(detected or behavioral),
            "detected_by":detected,"behavioral_case_failures":behavioral})
    return results

def baseline_analysis_checks(docs):
    text=docs["09_ORIGINAL_ANALYSIS.md"]
    blocks=re.findall(r"```text\n([^\n]+)\n```",text)
    style=re.findall(r"^\| S\d{2} \| ([^|]+) \|",text,re.M)
    exclude=re.findall(r"^\| X\d{2} \| ([^|]+) \|",text,re.M)
    ba=re.findall(r"^\| BA\d{2} .*",docs["06_SELECTION_CRITERIA.md"],re.M)
    return {
      "style_14_all_clauses_exact":len(style)==14 and len(blocks)==2
         and ", ".join(x.strip() for x in style)==blocks[0],
      "exclude_28_all_clauses_exact":len(exclude)==28 and len(blocks)==2
         and ", ".join(x.strip() for x in exclude)==blocks[1],
      "BA_8_complete_fields":len(ba)==8 and all(
         len(row.split("|")[1:-1])==6 and all(x.strip() for x in row.split("|")[1:-1])
         for row in ba)
    }


def product_record_checks(root,state):
    evidence=(root/"03_EVIDENCE_REGISTER.md").read_text(encoding="utf-8")
    report=(root/"10_PRODUCT_CAPABILITIES.md").read_text(encoding="utf-8")
    registered=set(re.findall(r"^### (SRC-\d{4})",evidence,re.M))
    external=state["external_source_ids"]
    internal=state.get("internal_recovery_source_ids",[])
    refs=set(re.findall(r"SRC-\d{4}",report))
    latest=state["workflow"]["latest_increment"]
    mismatch=[]
    for row in latest["impact"]:
        name=row["file"];path=root/name;kind=row["disposition"]
        if kind=="added":
            ok=path.is_file() and name not in latest["pre_edit_hashes"]
        else:
            changed=sha(path.read_bytes())!=latest["pre_edit_hashes"][name]
            ok=changed==(kind=="modified")
        if not ok:mismatch.append(name)
    questions=state.get("question_status",{})
    unresolved=any(questions.get("Q%02d"%n,{}).get("status")=="UNRESOLVED" for n in range(1,6))
    return {
      "increment_impact_matches":not mismatch,
      "external_count_and_registry_match":state["external_sources_count"]==len(set(external))==len(external)
          and registered==set(external)|set(internal),
      "report_source_refs_exist":refs.issubset(registered),
      "questions_all_recorded":set(questions)=={"Q%02d"%n for n in range(1,6)},
      "no_false_P1_complete":not unresolved or "partial" in state["stage_status"]["P1"],
      "audio_generation_still_zero":state["direct_audio_checks_count"]==state["generation_attempts_count"]==0
    }


def case_record_checks(root,state):
    evidence=(root/"03_EVIDENCE_REGISTER.md").read_text(encoding="utf-8")
    synthesis=(root/"11_CASE_RESEARCH.md").read_text(encoding="utf-8")
    source_ids=set(re.findall(r"^### (SRC-\d{4})",evidence,re.M))
    case_ids=set(re.findall(r"^### (CASE-\d{4})",evidence,re.M))
    records=state["p2_case_records"]
    actual={row["id"] for row in records}
    p2=state["p2_research_status"]
    return {
      "external_case_registry_matches":len(actual)==len(records)==state["external_case_report_count"]==11
          and case_ids==actual|{"CASE-0001"},
      "case_and_synthesis_sources_resolve":all(row["source_id"] in source_ids for row in records)
          and set(re.findall(r"SRC-\d{4}",synthesis)).issubset(source_ids),
      "incomplete_conditions_not_preset":state["complete_external_case_count"]==0
          and all(row["complete_conditions"] is False for row in records) and p2["preset_adopted"] is False,
      "public_pages_not_listening":state["direct_audio_checks_count"]==state["generation_attempts_count"]==0
          and all(row["direct_audio_check"] is False for row in records),
      "unresolved_effects_retained":p2["Q06"]==p2["Q07"]=="UNRESOLVED"
          and p2["effect_validated"] is False and "partial" in state["stage_status"]["P2"]
    }


def musical_record_checks(root,state):
    evidence=(root/"03_EVIDENCE_REGISTER.md").read_text(encoding="utf-8")
    report=(root/"12_MUSICAL_OPTIONS.md").read_text(encoding="utf-8")
    registered=set(re.findall(r"^### (SRC-\d{4})",evidence,re.M))
    expected=state["p3_option_ids"]
    option_pattern=r"^\| (OPT-[IRHMF]\d{2})\b"
    report_ids=re.findall(option_pattern,report,re.M)
    ledger_ids=re.findall(option_pattern,evidence,re.M)
    options=state["p3_option_records"]
    return {
      "option_ids_and_ledger_match":set(report_ids)==set(ledger_ids)==set(expected)
          and len(report_ids)==len(ledger_ids)==len(expected)==len(set(expected)),
      "sources_resolve_and_reuse_not_new":set(re.findall(r"SRC-\d{4}",report)).issubset(registered)
          and set(state["p3_new_source_ids"]).issubset(set(state["external_source_ids"]))
          and set(state["p3_reused_source_ids"]).isdisjoint(state["p3_new_source_ids"]),
      "D02_fields_complete":all(all(row.get(k) for k in ["design","expression","risk","sources"]) for row in options)
          and all(set(row["sources"]).issubset(registered) for row in options),
      "music_design_not_generation_evidence":all(row["kind"]=="AI_DESIGN_SYNTHESIS_FROM_E04"
          and row["decision"]=="READY_D02_MUSIC_SCOPE" and row["suno_effect"]=="UNVERIFIED" for row in options),
      "question_coverage_and_effect_limits":{row["question"] for row in options}=={"Q08","Q09","Q10","Q11"}
          and set(state["p3_question_status"])=={"Q08","Q09","Q10","Q11"}
          and all(q["status"]=="READY_D02_MUSIC_SCOPE" and q["suno_effect"]=="UNVERIFIED" for q in state["p3_question_status"].values()),
      "audio_generation_still_unperformed":state["direct_audio_checks_count"]==state["generation_attempts_count"]==0
    }


def comparison_plan_checks(root,state):
    evidence=(root/"03_EVIDENCE_REGISTER.md").read_text(encoding="utf-8")
    report=(root/"13_EVIDENCE_AND_TEST_PLAN.md").read_text(encoding="utf-8")
    sources=set(re.findall(r"^### (SRC-\d{4})",evidence,re.M))
    plans={r["id"]:r for r in state["p4_plan_records"]}
    claims={r["id"]:r for r in state["p4_claim_records"]}
    registered_plans=set(re.findall(r"^\| ((?:TST-\d{2}[A-Z]?|INT-\d{2})) \|",evidence,re.M))
    headed_plans=re.findall(r"^### ((?:TST-\d{2}[A-Z]?|INT-\d{2})) —",report,re.M)
    headed_claims=re.findall(r"^\| (P4-C\d{2}) ",report,re.M)
    caps=state["p4_proposed_request_caps"]
    return {
      "claim_and_plan_registry_match":set(claims)==set(state["p4_claim_ids"])==set(headed_claims)
          and set(plans)==set(state["p4_plan_ids"])==registered_plans==set(headed_plans)
          and len(headed_claims)==len(claims) and len(headed_plans)==len(plans),
      "sources_and_options_resolve":set(re.findall(r"SRC-\d{4}",report)).issubset(sources)
          and all(set(c["source_ids"]).issubset(sources) for c in claims.values())
          and all(set(p["option_ids"]).issubset(state["p3_option_ids"]) for p in plans.values()),
      "claim_plan_links_bidirectional":all(t in plans and cid in plans[t]["claim_ids"] for cid,c in claims.items() for t in c["test_ids"])
          and all(c in claims and pid in claims[c]["test_ids"] for pid,p in plans.items() for c in p["claim_ids"]),
      "comparison_fields_complete":all(all(p.get(k) for k in ["type","changed","a","b","fixed","observations","failure_and_limits","entry_gate"]) for p in plans.values())
          and all(all(c.get(k) for k in ["evidence","counter_and_limits","allowed_decision","status"]) for c in claims.values()),
      "planned_not_executed":all(p["status"]=="PLANNED_NOT_COMMITTED" and p["execution_count"]==0 for p in plans.values())
          and state["p4_status"]["actual_inputs_committed"] is False and state["p4_status"]["actual_executions"]==0
          and state["direct_audio_checks_count"]==state["generation_attempts_count"]==0,
      "proposed_caps_consistent":all(caps[k]["pilot"]+caps[k]["main"]==caps[k]["total"] for k in ["two_arm","three_model","interaction"])
          and caps["status"]=="DESIGN_PROPOSAL_NOT_CREDIT_AUTHORIZATION",
      "priority_resolves_and_no_criteria_change":state["p4_status"]["initial_plan_id"] in plans
          and state["p4_status"]["initial_model_priority"]=="v6-mini" and state["p4_status"]["criteria_changed"] is False
    }


def intake_record_checks(root,state):
    report=(root/"14_REQUEST_INTAKE.md").read_text(encoding="utf-8")
    evidence=(root/"03_EVIDENCE_REGISTER.md").read_text(encoding="utf-8")
    data=state["intake_process"]
    sources=set(re.findall(r"^### (SRC-\d{4})",evidence,re.M))
    ids=re.findall(r"^\| (IN-C\d{2}) \|",report,re.M)
    reqs=re.findall(r"^\| (IR\d{2}) \|",report,re.M)
    return {
      "intake_owner_and_refs":state["request_intake_document"]=="14_REQUEST_INTAKE.md"
          and state["workflow"]["owner_map"]["request_intake_and_direction"]==state["request_intake_document"]
          and set(re.findall(r"SRC-\d{4}",report)).issubset(sources),
      "requirements_scoped_and_registered":set(reqs)==set(data["requirements"])=={"IR01","IR02","IR03"}
          and state["requirement_count"]==22 and data["criteria_changed"] is False,
      "relation_and_clarity_axes_separate":data["relationship_states"]==["CONTINUE","CHANGE","NEW"]
          and data["clarity_states"]==["CLEAR","PARTIAL","UNDEFINED"]
          and all(x in report for x in ["기존 작업과의 관계","방향의 구체성","부분 아이디어"]),
      "profile_and_current_intake_consistent":data["common_process_not_music_profile"] is True
          and data["current_request"]["project_id"]==state["project_id"]
          and data["current_request"]["status"]=="READY_FOR_DESIGN"
          and data["current_request"]["new_music_decisions"] is False
          and data["current_request"]["reask_existing_requirements"] is False,
      "manual_cases_registered_not_actual_runs":len(ids)==len(set(ids))==9
          and set(ids)==set(data["manual_case_ids"]) and "TEST_ONLY" in report and "수동" in report,
      "handoff_and_execution_separate":all(x in report for x in data["handoff_states"])
          and "COMMIT-GATE" in report and "P5 전체" in report
          and ("partial" in state["stage_status"]["P5"] or (state.get("p5_workflow",{}).get("status")=="READY_DOCUMENT_SCOPE" and data.get("remaining_P5_work_status")=="RESOLVED_BY_15")) and bool(data["remaining_P5_work"]),
      "provenance_delegation_and_change_recorded":all(x in report for x in ["USER_FIXED","USER_PREFERENCE","AI_PROPOSED","OPEN","SUPERSEDED","brief_version","선택/위임","참고할 요소","따르지 않을 요소"]),
      "sources_are_scoped_method_references":set(data["source_ids"])=={"SRC-0084","SRC-0085"}
          and set(data["source_ids"]).issubset(state["external_source_ids"])
          and state["direct_audio_checks_count"]==state["generation_attempts_count"]==0
    }


def p5_route(case,defect=None):
    """Route supplied hypothetical review observations; does not classify music."""
    item=copy.deepcopy(case["input"])
    history=copy.deepcopy(case["history"])
    related=[h["id"] for h in history if h["project"]==item["project"] and h["lineage"]==item["lineage"]]
    audit=[h["id"] for h in history if h["project"]==item["project"] and h["status"] in {"rejected","held"}]
    novelty=[h["id"] for h in history if h["project"]==item["project"]
             and h["lineage"]!=item["lineage"] and h["status"] in {"active_design","adopted_output"}]
    if defect=="drop_nonadjacent":novelty=[h for h in novelty if h!="SIM-H04"]
    closest=item["closest_id"]
    issues=[]
    if item["mandatory_conflict"]:issues.append("MANDATORY_DESIGN_CONFLICT")
    if not item["design_complete"]:issues.append("MISSING_DESIGN_FIELDS")
    if item["history_scope"]=="METADATA_ONLY":issues.append("MISSING_HISTORY_FEATURES")
    if item["body_distinction"] in {"nominal","intro_only"}:issues.append("NO_PERSISTENT_DESIGN_DISTINCTION")
    if item["direct_audio_checked"] and item["audio_distinction"]=="SAME":issues.append("SIMULATED_OUTPUT_BODY_SAME")
    if item["sequence_review"]=="CONFIRMED_CONFLICT":issues.append("SIMULATED_CUMULATIVE_CONFLICT")
    if item["mandatory_conflict"]:status="REVISE_DESIGN"
    elif not item["design_complete"]:status="HOLD_D06"
    elif defect=="require_reference_for_design" and not item["reference_audio_available"]:status="HOLD_D06"
    elif item["history_scope"]=="NO_REGISTERED_HISTORY":status="SEED_ONLY"
    elif item["history_scope"]=="METADATA_ONLY" or closest not in novelty:status="HOLD_D06"
    elif item["body_distinction"] in {"nominal","intro_only"} and defect!="skip_nominal_check":status="REVISE_DESIGN"
    elif item["body_distinction"]=="unknown" or not item["distinction_reason"]:status="HOLD_D06"
    elif item["direct_audio_checked"] and item["audio_distinction"]=="SAME":status="REVISE_AUDIO_DISTINCTION"
    elif item["sequence_review"]=="CONFIRMED_CONFLICT":status="REVISE_SEQUENCE"
    elif item["sequence_review"]=="RISK":status="REVIEW_SEQUENCE"
    else:status="DESIGN_PASS_SCOPED"
    design=("HOLD_D06" if status=="HOLD_D06" else "SEED_ONLY" if status=="SEED_ONLY"
            else "REVISE_DESIGN" if status=="REVISE_DESIGN" else "DESIGN_PASS_SCOPED")
    actions={
      "DESIGN_PASS_SCOPED":"P6_DESIGN_TO_INPUT_PREPARATION",
      "REVISE_DESIGN":"REVISE_CAUSAL_DESIGN_RELATION_AND_VERSION",
      "HOLD_D06":"RECOVER_MISSING_COMPARISON_ONLY",
      "SEED_ONLY":"PRESERVE_SEED_AND_COMPARE_WHEN_NEXT_CANDIDATE_EXISTS",
      "REVISE_AUDIO_DISTINCTION":"REVIEW_OUTPUT_AND_DESIGN_INPUT_LINK",
      "REVISE_SEQUENCE":"REVIEW_SEQUENCE_EXPOSURE_AND_AFFECTED_TRACKS",
      "REVIEW_SEQUENCE":"PLAN_SCOPED_CUMULATIVE_CHECK"}
    record={
      "test_only":True,"case_id":case["id"],"request_id":"SIM-INTAKE",
      "project_id":item["project"],"playlist_id":item["playlist"],
      "lineage_id":item["lineage"],"design_version":item["version"],
      "supersedes":item["previous_version_id"],"criteria_owner":"06_SELECTION_CRITERIA.md",
      "search_scope":item["history_scope"],
      "queried_ids":[h["id"] for h in history if h["project"]==item["project"]],
      "novelty_candidates":novelty,"failure_audit_ids":audit,"related_versions":related,
      "closest_id":closest,"closest_selection":"provided hypothetical reviewer observation; not automatic nearest-music ranking",
      "comparison_reason":item["distinction_reason"],"issue_flags":issues,
      "design_state":design,"summary_state":status,
      "input_readiness":"NEXT_GATE_REQUIRED" if item["account_fields_ready"] else "HOLD_ACCOUNT_FIELDS",
      "hypothetical_D05_gate":"OBSERVATION_REQUIRED" if item["reference_audio_available"] else "HOLD_REFERENCE",
      "actual_audio_status":"NOT_TESTED","adoption_state":"NOT_ADOPTED",
      "actual_generation_requested":False,"actual_track_count":0,
      "next_action":actions[status]}
    return record

def p5_procedure_checks(root,state,out):
    data=json.loads((root/"p5_workflow_cases.json").read_text(encoding="utf-8"))
    doc=(root/"15_REPEATABLE_PRODUCTION_WORKFLOW.md").read_text(encoding="utf-8")
    ledger=(root/"03_EVIDENCE_REGISTER.md").read_text(encoding="utf-8")
    spec=state["p5_workflow"]
    rows_out=[]
    for case in data["cases"]:
        before=copy.deepcopy(case["history"])
        record=p5_route(case)
        old_bytes=json.dumps(before,ensure_ascii=False,sort_keys=True)
        packet={"test_only":True,"source_history":before,"new_review_record":record}
        # Round-trip each record through a real file; the one final report retains every case.
        path=out/"p5_dry_run.json"
        path.write_text(json.dumps(packet,ensure_ascii=False,indent=2),encoding="utf-8")
        loaded=json.loads(path.read_text(encoding="utf-8"))
        failures=[]
        if record["summary_state"]!=case["expected"]:failures.append("summary_state")
        if loaded["new_review_record"]!=record:failures.append("record_round_trip")
        if json.dumps(loaded["source_history"],ensure_ascii=False,sort_keys=True)!=old_bytes:failures.append("history_changed")
        expected_novelty={h["id"] for h in before if h["project"]==case["input"]["project"]
            and h["lineage"]!=case["input"]["lineage"] and h["status"] in {"active_design","adopted_output"}}
        if set(record["novelty_candidates"])!=expected_novelty:failures.append("retrieval_scope")
        if case["id"]=="P5-C07" and record["hypothetical_D05_gate"]!="HOLD_REFERENCE":failures.append("reference_gate")
        if case["id"]=="P5-C11":
            if record["design_version"]!=2 or record["supersedes"] not in record["related_versions"]:failures.append("version_chain")
        if case["id"]=="P5-C12" and record["input_readiness"]!="HOLD_ACCOUNT_FIELDS":failures.append("account_gate")
        if case["id"]=="P5-C08" and record["design_state"]!="DESIGN_PASS_SCOPED":failures.append("design_vs_output")
        rows_out.append({"id":case["id"],"passed":not failures,"failures":failures,
                         "input":case,"output":record,"history_preserved":loaded["source_history"]==before})
    by_id={c["id"]:c for c in data["cases"]}
    probes=[("drop_nonadjacent","P5-C10"),("skip_nominal_check","P5-C02"),("require_reference_for_design","P5-C07")]
    mutants=[{"defect":d,"case_id":cid,"rejected":p5_route(by_id[cid],d)["summary_state"]!=by_id[cid]["expected"]} for d,cid in probes]
    document_ids=re.findall(r"^\| (P5-C\d{2}) \|",doc,re.M)
    checks={
      "fixed_fixture_hash":sha((root/"p5_workflow_cases.json").read_bytes())==spec["cases_sha256"],
      "case_ids_and_document_match":len(document_ids)==len(set(document_ids))==13
          and set(document_ids)==set(spec["case_ids"])==set(by_id),
      "owners_and_source_refs":state["repeatable_workflow_document"]==spec["document"]
          and state["workflow"]["owner_map"]["repeatable_production_workflow"]==spec["document"]
          and set(re.findall(r"SRC-\d{4}",doc)).issubset(set(re.findall(r"^### (SRC-\d{4})",ledger,re.M))),
      "record_schema_connected":all(x in (root/"04_PRODUCTION_HISTORY.md").read_text(encoding="utf-8")
          for x in ["search_scope","failure_audit_ids","related_versions","D06_scope","lineage_id"]),
      "scope_and_counts_preserved":spec["criteria_changed"] is False and spec["test_only"] is True
          and spec["actual_tracks_registered"]==spec["actual_executions"]==0
          and state["direct_audio_checks_count"]==state["generation_attempts_count"]==0,
      "no_false_P5_execution_event":spec["status"]=="READY_DOCUMENT_SCOPE"
          and state["intake_process"]["remaining_P5_work_status"]=="RESOLVED_BY_15"
          and "no_actual_generation_pass_event" in state["stage_status"]["P5"],
      "hypothetical_routes_and_roundtrip":all(r["passed"] for r in rows_out),
      "known_P5_defects_rejected":all(m["rejected"] for m in mutants)}
    detail={"test_only":True,"scope":"Given hypothetical review facts; no music classifier or independent AI execution",
            "checks":checks,"cases":rows_out,"mutation_tests":mutants}
    (out/"p5_dry_run.json").write_text(json.dumps(detail,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return checks,rows_out,mutants


def p6_design_integrity(data,state,root):
    tracks=data["tracks"];ids=[t["id"] for t in tracks];idset=set(ids)
    expected={"TRK-%06d"%i for i in range(1,21)}
    doc=(root/"16_FIRST_BATCH_DESIGNS.md").read_text(encoding="utf-8")
    ledger=(root/"03_EVIDENCE_REGISTER.md").read_text(encoding="utf-8")
    options=(root/"12_MUSICAL_OPTIONS.md").read_text(encoding="utf-8")
    optids=set(re.findall(r"^\| (OPT-[A-Z]\d{2}) ",options,re.M))
    sources=set(re.findall(r"^### (SRC-\d{4})",ledger,re.M))
    pairs={(r["a"],r["b"]) for r in data["pairwise_screen"]}
    expected_pairs={(ids[a],ids[b]) for a in range(len(ids)) for b in range(a+1,len(ids))}
    adj=[(e["from"],e["to"]) for e in data["adjacent_reviews"]]
    body_fields=["motif","rhythm_and_rests","bass_relation","body_development"]
    fingerprints=[tuple(t.get(k) for k in body_fields) for t in tracks]
    pc={"C":0,"Db":1,"D":2,"Eb":3,"E":4,"F":5,"Gb":6,"G":7,"Ab":8,"A":9,"Bb":10,"B":11}
    chord_intervals={"maj7":[0,4,7,11],"m7":[0,3,7,10],"6":[0,4,7,9]}
    harmonic_errors=[]
    for t in tracks:
        tonic,mode=t["key"].split()
        scale={((pc[tonic]+i)%12) for i in ([0,2,4,5,7,9,11] if mode=="major" else [0,2,3,5,7,8,10])}
        for h in t["harmonic_cycle"]:
            chord,*bass=h["chord"].split("/")
            m=re.fullmatch(r"([A-G](?:b)?)(maj7|m7|6)",chord)
            if not m:harmonic_errors.append(t["id"]+":unsupported_chord");continue
            tones={(pc[m[1]]+i)%12 for i in chord_intervals[m[2]]}
            if not tones.issubset(scale):harmonic_errors.append(t["id"]+":outside_scale")
            if bass and pc[bass[0]] not in tones:harmonic_errors.append(t["id"]+":nonchord_slash_bass")
    register=(root/"04_PRODUCTION_HISTORY.md").read_text(encoding="utf-8")
    fields=["working_label","key","meter","harmonic_cycle","motif","rhythm_and_rests","groove","bass_relation","roles","opening","body_development","ending","keyboard_plan","risk_ids","risk_action","option_ids","source_ids","closest_id","closest_reason","history_scope"]
    return {
      "twenty_actual_designs_unique_registered":len(ids)==len(idset)==20 and idset==expected
          and sorted(t["order"] for t in tracks)==list(range(1,21))
          and set(state["p6_designs"]["track_ids"])==expected
          and all(re.search(r"^\| "+re.escape(i)+r" \|",register,re.M) for i in ids),
      "required_design_fields_and_refs":all(all(t.get(k) for k in fields) for t in tracks)
          and all(set(t["option_ids"]).issubset(optids) and set(t["source_ids"]).issubset(sources) for t in tracks)
          and all(t["closest_id"] in idset-{t["id"]} for t in tracks),
      "all_pair_and_neighbor_scope":len(data["pairwise_screen"])==190 and pairs==expected_pairs
          and len(adj)==19 and adj==list(zip(ids[:-1],ids[1:])),
      "exact_body_clone_screen":len(fingerprints)==len(set(fingerprints)),
      "cycle_lengths_and_diatonic_harmony":all(sum(h["bars"] for h in t["harmonic_cycle"])==8 for t in tracks) and not harmonic_errors,
      "target_duration_proposal_totals":sum(t["target_duration_seconds"] for t in tracks)==data["target_duration_seconds"]==3600
          and all(t["bpm_proposal"]>0 and t["target_duration_seconds"]>0 for t in tracks),
      "keyboard_roles_and_sequence_consistent":all(t["keyboard_role"] in {"MAIN","BACKGROUND","NONE"} for t in tracks)
          and all(data["keyboard_exposure"][k]==[t["id"] for t in tracks if t["keyboard_role"]==r]
                  for k,r in [("main_ids","MAIN"),("background_ids","BACKGROUND"),("none_ids","NONE")])
          and all(not(a["keyboard_role"]==b["keyboard_role"]=="MAIN") for a,b in zip(tracks,tracks[1:])),
      "statuses_and_scope_not_inflated":data["test_only"] is False and data["history"]["prior_user_catalog"]=="UNAVAILABLE"
          and all(t["design_status"]=="DESIGN_PASS_SCOPED" and t["input_status"]==({"TRK-000001":state["track01_input"]["status"],"TRK-000002":state["track02_input"]["status"]}.get(t["id"],"NOT_WRITTEN"))
                  and t["audio_status"]=="NOT_ASSESSED" and t["actual_output_ids"]==[] for t in tracks)
          and state["registered_track_designs_count"]==20 and state["generation_attempts_count"]==0
          and "partial" in state["stage_status"]["P6"],
      "readable_view_and_record_id_alignment":all(("### %02d."%t["order"]) in doc and t["id"] in doc
          and t["motif"] in doc and t["closest_reason"] in doc for t in tracks),
      "existing_criteria_retained":state["p6_designs"]["criteria_changed"] is False
          and state["requirements_semantic_version"]=="0.4" and state["criteria_version"]=="0.4.2"
    }

def p6_design_checks(root,state):
    data=json.loads((root/"first_batch_designs.json").read_text(encoding="utf-8"))
    checks=p6_design_integrity(data,state,root)
    mutated=[]
    clone=copy.deepcopy(data)
    for k in ["motif","rhythm_and_rests","bass_relation","body_development"]:clone["tracks"][1][k]=clone["tracks"][0][k]
    mutated.append({"defect":"body_clone_despite_different_key_instrument","rejected":not p6_design_integrity(clone,state,root)["exact_body_clone_screen"]})
    missing=copy.deepcopy(data);missing["tracks"][0]["closest_id"]="TRK-999999"
    mutated.append({"defect":"missing_closest_track_reference","rejected":not p6_design_integrity(missing,state,root)["required_design_fields_and_refs"]})
    pair=copy.deepcopy(data);pair["pairwise_screen"].pop()
    mutated.append({"defect":"one_pair_omitted","rejected":not p6_design_integrity(pair,state,root)["all_pair_and_neighbor_scope"]})
    harmony=copy.deepcopy(data);harmony["tracks"][0]["harmonic_cycle"][0]["chord"]="Gbmaj7"
    mutated.append({"defect":"unintended_out_of_key_chord","rejected":not p6_design_integrity(harmony,state,root)["cycle_lengths_and_diatonic_harmony"]})
    return checks,mutated



def design_music_digest(data):
    tracks=[{k:v for k,v in x.items() if k not in {"input_status","input_package_id","prompt_record_id","actual_output_ids","observed_output_ids"}} for x in data["tracks"]]
    return sha(json.dumps(tracks,ensure_ascii=False,sort_keys=True))

def preinput_gate(root,state,prompt_id):
    current_lead=state.get("lead_instrument_policy")
    if current_lead:
        entry=next((e for e in state["prompt_register"]["entries"] if e["id"]==prompt_id),None)
        if entry and entry.get("current_use_status") in {"DO_NOT_REUSE_GUITAR_MAIN","HOLD_KEYBOARD_MAIN_REVIEW"}:
            return {"allowed":False,"status":entry["current_use_status"],"requirement":"R23",
                "reason":"Current project keeps piano/keyboard main; old text cannot be reused without a complete reviewed revision"}
    policy=state["prompt_input_policy"]
    entries=state["prompt_register"]["entries"]
    entry=next((e for e in entries if e["id"]==prompt_id and e["complete"]),None)
    candidate=next((p for p in policy["packages"] if p["prompt_id"]==prompt_id),None)
    if not entry or not candidate:
        return {"allowed":False,"status":"BLOCKED","checks":{"registered_complete_package":False}}
    package=state["track01_input"] if candidate["package_id"]==state["track01_input"]["id"] else state.get(candidate.get("input_state_key",""),candidate.get("input",{}))
    style=package.get("style","");exclude=package.get("exclude","")
    controls=package.get("actual_controls")
    source_text=(root/candidate["source_document"]).read_text(encoding="utf-8")
    receipts=[r for r in policy["receipts"] if r.get("prompt_id")==prompt_id and r.get("version")==entry["version"]]
    receipt=receipts[-1] if receipts else {}
    required_prompts={e["id"]:e["version"] for e in entries if e["complete"] and e["id"]!=prompt_id}
    designs=json.loads((root/"first_batch_designs.json").read_text(encoding="utf-8"))
    # Current project has20 designs, pinned together by their source digest.
    required_designs={"TRK-%06d"%i for i in range(1,21)}
    duplicates=[e for e in entries if e["complete"] and e["id"]!=prompt_id and
        e.get("style_sha256")==sha(style) and e["lineage_id"]!=entry["lineage_id"]]
    content=receipt.get("content_review",{})
    checks={
      "review_present":bool(receipt.get("reviewed_at")) and receipt.get("status")=="PASS_SCOPED",
      "standard_current":receipt.get("standard_sha256")==sha((root/policy["standard_document"]).read_bytes()),
      "register_current":receipt.get("register_sha256")==sha((root/policy["register_document"]).read_bytes()),
      "designs_current":receipt.get("designs_music_sha256")==design_music_digest(designs),
      "prompt_current":bool(style and exclude) and receipt.get("style_sha256")==sha(style)==entry.get("style_sha256")
          and receipt.get("exclude_sha256")==sha(exclude)==entry.get("exclude_sha256"),
      "package_source_matches":style in source_text and exclude in source_text,
      "lyrics_current":receipt.get("lyrics_sha256")==sha(package.get("lyrics","")),
      "settings_current":controls is not None and receipt.get("settings_sha256")==sha(json.dumps(controls,ensure_ascii=False,sort_keys=True)),
      "known_history_covered":all(receipt.get("compared_prompt_versions",{}).get(k)==v for k,v in required_prompts.items())
          and required_designs.issubset(set(receipt.get("compared_design_ids",[]))),
      "content_review_recorded":all(isinstance(content.get(k),str) and content[k].strip()
          for k in ["shared_atmosphere","closest_prompt_or_design","intro_difference","body_difference","timbre_difference","coverage_limit"]),
      "mandatory_conflicts_resolved":receipt.get("mandatory_conflicts") == [],
      "no_other_track_exact_duplicate":not duplicates,
      "within_observed_advanced_limits":controls is not None and controls.get("mode")=="Advanced"
          and len(style)<=state["account_input_limits"]["advanced_style_max_chars"]
          and len(exclude)<=state["account_input_limits"]["exclude_max_chars"],
      "version_package_match":candidate["version"]==entry["version"] and package.get("version")==entry["version"],
      "reuse_reason":receipt.get("operation")!="reuse" or bool(receipt.get("intentional_reuse_reason"))
    }
    return {"allowed":all(checks.values()),"status":"PASS_SCOPED" if all(checks.values()) else "BLOCKED","checks":checks,
        "scope":"Input readiness; not generation authorization or audio distinction"}

def prompt_register_checks(root,state):
    reg=(root/"18_PROMPT_REGISTER.md").read_text(encoding="utf-8")
    baseline=(root/"09_ORIGINAL_ANALYSIS.md").read_text(encoding="utf-8")
    fence=chr(96)*3
    old=re.findall(fence+r"text\n(.*?)\n"+fence,baseline,re.S)
    full=re.findall(fence+r"text\n(.*?)\n"+fence,reg,re.S)
    pkg=state["track01_input"];entries=state["prompt_register"]["entries"]
    known={e["id"]:e["version"] for e in entries if e["complete"] and e["id"]!="PRM-000002"}
    checks={
      "exact_full_texts_and_order":full==[old[0],old[1],pkg["style"],pkg["exclude"],state["track02_input"]["style"],state["track02_input"]["exclude"]],
      "complete_partial_missing_scoped":state["prompt_register"]["complete_prompt_count"]==3
          and state["prompt_register"]["partial_prompt_count"]==1 and state["prompt_register"]["missing_legacy_batch_count"]==20
          and sum(bool(e["complete"]) for e in entries)==3,
      "source_hashes_match":all(e["style_sha256"]==sha(full[i*2]) and e["exclude_sha256"]==sha(full[i*2+1])
          for i,e in enumerate([e for e in entries if e["complete"]])),
      "entry_and_procedure_linked":all("18_PROMPT_REGISTER.md" in (root/n).read_text(encoding="utf-8")
          for n in ["00_START_HERE.md","04_PRODUCTION_HISTORY.md","05_DECISIONS_AND_PROGRESS.md","15_REPEATABLE_PRODUCTION_WORKFLOW.md"])
          and "## 12. Suno Style" in (root/"15_REPEATABLE_PRODUCTION_WORKFLOW.md").read_text(encoding="utf-8"),
      "no_retroactive_review":state["prompt_input_policy"]["retroactive_compliance_claim"] is False
          and not any(r.get("prompt_id")=="PRM-000002" for r in state["prompt_input_policy"]["receipts"]),
      "music_and_inputs_retained":all(sha((root/n).read_bytes())==state["workflow"]["latest_increment"]["pre_edit_hashes"][n]
          for n in ["02_PRODUCTION_STANDARD.md","06_SELECTION_CRITERIA.md","09_ORIGINAL_ANALYSIS.md","17_TRACK01_INPUT.md","16_FIRST_BATCH_DESIGNS.md"]) and sha(json.dumps([{k:v for k,v in x.items() if k not in {"input_status","input_package_id","prompt_record_id"}} for x in json.loads((root/"first_batch_designs.json").read_text(encoding="utf-8"))["tracks"]],ensure_ascii=False,sort_keys=True))==state["workflow"]["latest_increment"]["pre_design_music_sha256"],
    }
    sample=copy.deepcopy(state)
    receipt={"prompt_id":"PRM-000002","version":"1.0","status":"PASS_SCOPED","reviewed_at":"TEST_ONLY",
       "standard_sha256":sha((root/"02_PRODUCTION_STANDARD.md").read_bytes()),
       "register_sha256":sha((root/"18_PROMPT_REGISTER.md").read_bytes()),
       "designs_music_sha256":design_music_digest(json.loads((root/"first_batch_designs.json").read_text(encoding="utf-8"))),
       "style_sha256":sha(pkg["style"]),"exclude_sha256":sha(pkg["exclude"]),"lyrics_sha256":sha(pkg.get("lyrics","")),
       "settings_sha256":sha(json.dumps(pkg["actual_controls"],ensure_ascii=False,sort_keys=True)),
       "compared_prompt_versions":known,"compared_design_ids":["TRK-%06d"%i for i in range(1,21)],
       "content_review":{k:"TEST_ONLY hypothetical supplied content-review fact" for k in
          ["shared_atmosphere","closest_prompt_or_design","intro_difference","body_difference","timbre_difference","coverage_limit"]},
       "mandatory_conflicts":[],"operation":"new"}
    sample["prompt_input_policy"]["receipts"]=[receipt]
    cases=[]
    def case(name,changed,expected):
        result=preinput_gate(root,changed,"PRM-000002")
        cases.append({"id":name,"test_only":True,"expected_allowed":expected,
            "actual_allowed":result["allowed"],"passed":result["allowed"]==expected})
    case("valid_scoped_record",sample,True)
    case("missing_review_blocks_actual_current",state,False)
    stale=copy.deepcopy(sample);stale["prompt_input_policy"]["receipts"][0]["standard_sha256"]="stale"
    case("changed_standard_invalidates_review",stale,False)
    missing=copy.deepcopy(sample);missing["prompt_input_policy"]["receipts"][0]["compared_prompt_versions"]={}
    case("unread_history_blocks",missing,False)
    conflict=copy.deepcopy(sample);conflict["prompt_input_policy"]["receipts"][0]["mandatory_conflicts"]=["TEST_ONLY"]
    case("mandatory_conflict_blocks",conflict,False)
    dup=copy.deepcopy(sample);dup["prompt_register"]["entries"][0]["style_sha256"]=sha(pkg["style"])
    case("same_prompt_other_track_blocks",dup,False)
    reuse=copy.deepcopy(dup);reuse["prompt_register"]["entries"][0]["lineage_id"]="TRK-000001"
    reuse["prompt_input_policy"]["receipts"][0]["operation"]="reuse"
    case("same_track_reuse_requires_reason",reuse,False)
    reuse["prompt_input_policy"]["receipts"][0]["intentional_reuse_reason"]="TEST_ONLY deliberate same-track refill"
    case("same_track_documented_reuse_allowed",reuse,True)
    checks["gate_branch_cases"]=all(c["passed"] for c in cases)
    return checks,cases



def batch_record_checks(root,state):
    import zipfile
    from datetime import datetime
    batch=state["batch_generation"];pkgs=batch["packages"];reqs=batch["requests"]
    register=(root/"18_PROMPT_REGISTER.md").read_text(encoding="utf-8")
    report=(root/"19_BATCH_GENERATION.md").read_text(encoding="utf-8")
    standard=(root/"02_PRODUCTION_STANDARD.md").read_text(encoding="utf-8")
    criteria=(root/"06_SELECTION_CRITERIA.md").read_text(encoding="utf-8")
    fixtures=json.loads((root/"workflow_cases.json").read_text(encoding="utf-8"))
    baseline=state["workflow"]["baseline"]
    designs=json.loads((root/"first_batch_designs.json").read_text(encoding="utf-8"))
    with zipfile.ZipFile(root.parent/"suno_lofi_research_v0.16.0.zip") as z:
        prior_designs=json.loads(z.read("first_batch_designs.json"))
        prior_report=json.loads(z.read("workflow_validation.json"))
    fence=chr(96)*3
    old=re.findall(fence+r"text\n(.*?)\n"+fence,(root/"09_ORIGINAL_ANALYSIS.md").read_text(encoding="utf-8"),re.S)
    full=re.findall(fence+r"text\n(.*?)\n"+fence,register,re.S)
    expected=[old[0],old[1],state["track01_input"]["style"],state["track01_input"]["exclude"],state["track02_input"]["style"],state["track02_input"]["exclude"]]
    for pkg in pkgs:expected.extend([pkg["style"],pkg["exclude"]])
    def fnv(text):
        h=2166136261
        for c in text:h=((h^ord(c))*16777619)&0xffffffff
        return h
    pmap={x["track"]:x for x in pkgs};omap={x["track"]:x for x in reqs}
    outputs=[o for req in reqs for o in req["outputs"]]
    all_urls=[o["url"] for o in outputs]+[u for e in batch["preexisting_outputs"] for u in e["urls"]]
    actual_refs={e["name"]:e["library_file_id"] for e in state["authoritative_file_refs"]}
    controls=batch["controls"];review=batch["review"]
    intro_time=datetime.fromisoformat(review["reviewed_at"])
    times=[datetime.fromisoformat(r["create_started_at"].replace("Z","+00:00")) for r in reqs]
    traceable=all(r["track"] in pmap and r["package_id"]==pmap[r["track"]]["package_id"]
        and r["prompt_id"]==pmap[r["track"]]["prompt_id"] and r["input_exact"]
        and r["style_fnv"]==fnv(pmap[r["track"]]["style"])
        and r["exclude_fnv"]==fnv(pmap[r["track"]]["exclude"]) for r in reqs)
    return {
      "requirements_T_G_preserved":sha("\n".join(rows(standard,r"^\| R\d{2} \|")))==baseline["requirements_sha256"]
          and sha("\n".join(rows(criteria,r"^\| T\d{2} \|")))==baseline["T_sha256"]
          and sha("\n".join(rows(criteria,r"^\| G\d{2} ")))==baseline["G_sha256"],
      "original_fixed_cases_preserved":sha((root/"workflow_cases.json").read_bytes())==baseline["cases_sha256"]
          and sha((root/"p5_workflow_cases.json").read_bytes())=="46efd42c96d6a93588e72906812a7e6f0a1e1e797c08f76e2a18d924f8e36279",
      "twenty_musical_designs_preserved":design_music_digest(designs)==design_music_digest(prior_designs),
      "old_inputs_exact_new_registry_complete":full==expected and len(full)==42
          and state["prompt_register"]["complete_prompt_count"]==21,
      "new_package_limits_and_exclusions":len(pkgs)==18 and all(len(x["style"])<=1000 and len(x["exclude"])<=1000
          and (x["exclude"]==old[1] or x["exclude"]==old[1]+", piano, electric piano, Rhodes, keyboard leads") for x in pkgs),
      "review_precedes_requests_and_versions_current":intro_time<=min(times) and review["status"]=="PASS_SCOPED"
          and review["standard_sha256"]==sha((root/"02_PRODUCTION_STANDARD.md").read_bytes())
          and review["register_sha256"]==sha((root/"18_PROMPT_REGISTER.md").read_bytes()),
      "actual_input_traceability":traceable,
      "exactly18_single_requests_no_reroll":len(reqs)==len(set(r["track"] for r in reqs))==18
          and set(omap)==set(range(3,21)) and all(r["retry_count"]==0 for r in reqs)
          and batch["max_create_requests"]==18 and batch["rerolls_performed"]==0,
      "all36_outputs_returned_unique":len(outputs)==len({o["id"] for o in outputs})==36
          and all(len(r["outputs"])==2 and r["status"]=="TWO_OUTPUTS_RETURNED" for r in reqs),
      "all_outputs_have_real_links_displayed_length":all(re.fullmatch(r"https://suno.com/song/[0-9a-f-]{36}",o["url"])
          and o["url"].endswith(o["id"]) and re.fullmatch(r"\d+:\d{2}",o["displayed_duration"])
          and o["displayed_duration"]!="0:00" for o in outputs),
      "forty_candidate_links_in_feedback_document":len(all_urls)==len(set(all_urls))==40 and all(u in report for u in all_urls),
      "preexisting_candidates_not_agent_requests":{x["track"] for x in batch["preexisting_outputs"]}=={1,2}
          and all(x["actor"]=="PREEXISTING_UNKNOWN" for x in batch["preexisting_outputs"]),
      "settings_and_empty_lyrics":controls["mode"]=="Advanced" and controls["model"]=="v6-mini"
          and controls["weirdness"]==50 and controls["style_influence"]==50 and controls["variety"]==0
          and controls["max_mode"]=="Off" and controls["length"]=="Auto" and controls["personalization"]=="Off"
          and all(x["lyrics"]=="" and x["controls"]==controls for x in pkgs)
          and all(r["actual_controls"]==controls for r in reqs),
      "generation_count_and_output_register_agree":state["generation_attempts_count"]==len(reqs)==batch["create_requests_actual"]==18
          and state["registered_generated_output_count"]==batch["outputs_returned_count"]==36
          and all(set(x["actual_output_ids"])=={o["id"] for o in omap[x["order"]]["outputs"]} for x in designs["tracks"][2:]),
      "credit_observation_not_false_free_or_purchase":batch["credit_decrease_observed"]==180 and batch["purchases_allowed"] is False
          and all(r["credit_cost_individual"]=="NOT_INDIVIDUALLY_OBSERVED" for r in reqs),
      "feedback_separate_from_audio_adoption":state["direct_audio_checks_count"]==0 and state["adopted_tracks_count"]==0
          and all(x["audio_status"]=="NOT_ASSESSED" and x["adoption_status"]=="NOT_ADOPTED" for x in designs["tracks"])
          and batch["status"]=="COMPLETE_WAIT_USER_FEEDBACK",
      "canonical_refs_resolve":set(actual_refs)==set(state["authoritative_documents"])|{"project_state.json"}
          and len(set(actual_refs.values()))==len(actual_refs)
          and all((root/n).is_file() and re.fullmatch(r"libfile_[0-9a-f]+",v) for n,v in actual_refs.items()),
      "past_verification_preserved_not_relabelled":prior_report["passed"] and prior_report["validator_version"]=="0.16.0"
          and prior_report["test_only"] is True,
    }

def validate_batch_release(root,state,out,publication):
    checks=batch_record_checks(root,state)
    # Given-case routing still runs on the original unchanged fixture and current definitions.
    fixtures=json.loads((root/"workflow_cases.json").read_text(encoding="utf-8"))
    docs={n:(root/n).read_text(encoding="utf-8") for n in CORE if n.endswith(".md")}
    cases=case_results(fixtures["cases"],docs,state,out)
    mutant_results=[]
    for label,mutator,key in [
      ("missing_returned_candidate",lambda s:s["batch_generation"]["requests"][0]["outputs"].pop(),"all36_outputs_returned_unique"),
      ("duplicated_request",lambda s:s["batch_generation"]["requests"].append(copy.deepcopy(s["batch_generation"]["requests"][0])),"exactly18_single_requests_no_reroll"),
      ("wrong_input_fingerprint",lambda s:s["batch_generation"]["requests"][0].update(style_fnv=0),"actual_input_traceability"),
      ("duplicate_output_url",lambda s:s["batch_generation"]["requests"][0]["outputs"][1].update(id=s["batch_generation"]["requests"][0]["outputs"][0]["id"],url=s["batch_generation"]["requests"][0]["outputs"][0]["url"]),"all36_outputs_returned_unique")]:
        mutant=copy.deepcopy(state);mutator(mutant)
        rejected=not batch_record_checks(root,mutant)[key]
        mutant_results.append({"test_only":True,"defect":label,"rejected":rejected})
    passed=all(checks.values()) and all(x["passed"] for x in cases) and all(x["rejected"] for x in mutant_results)
    report={"validator_version":VERSION,"scope":"Actual UI generation record integrity and preserved document criteria; not music/audio quality",
        "test_only":False,"passed":passed,"batch_record_checks":checks,
        "cases":[{"id":x["case_id"],"passed":x["passed"],"test_only":True} for x in cases],
        "mutation_tests":mutant_results,"actual_counts":{"requests":18,"new_outputs":36,"all_candidates":40,"observed_credit_decrease":180},
        "limitations":["Individual charge updates asynchronous; total observed decrease recorded","Displayed durations are not measured downloaded audio","User audio feedback/adoption pending"],
        "release_decision":"PASS_BATCH_OUTPUT_RECORD_SCOPE" if passed else "REJECT"}
    payload=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    (root/"workflow_validation.json").write_text(payload,encoding="utf-8")
    (out/"batch_generation.json").write_text(payload,encoding="utf-8")
    (out/"summary.json").write_text(payload,encoding="utf-8")
    print(json.dumps({"passed":passed,"checks":len(checks),"failed":[k for k,v in checks.items() if not v],"fixture_cases_passed":sum(c["passed"] for c in cases),"defects_rejected":sum(m["rejected"] for m in mutant_results),"decision":report["release_decision"]},ensure_ascii=False))
    return 0 if passed else 1



def validate_lead_feedback(root,state,out):
    import zipfile
    policy=state["lead_instrument_policy"]
    with zipfile.ZipFile(root.parent/"suno_lofi_research_v0.17.0.zip") as z:
        old=json.loads(z.read("project_state.json"))
        old_prompts=re.findall(chr(96)*3+r"text\n(.*?)\n"+chr(96)*3,z.read("18_PROMPT_REGISTER.md").decode("utf-8").replace("\r\n","\n"),re.S)
        old_results=z.read("19_BATCH_GENERATION.md").decode("utf-8")
        old_report=json.loads(z.read("workflow_validation.json"))
    standard=(root/"02_PRODUCTION_STANDARD.md").read_text(encoding="utf-8")
    criteria=(root/"06_SELECTION_CRITERIA.md").read_text(encoding="utf-8")
    rrows=rows(standard,r"^\| R\d{2} \|")
    old_rrows=[r for r in rrows if not r.startswith("| R23 |")]
    all_rids=[r.split("|")[1].strip() for r in rrows]
    designs=json.loads((root/"first_batch_designs.json").read_text(encoding="utf-8"))
    prompts=(root/"18_PROMPT_REGISTER.md").read_text(encoding="utf-8")
    results=(root/"19_BATCH_GENERATION.md").read_text(encoding="utf-8")
    current_prompts=re.findall(chr(96)*3+r"text\n(.*?)\n"+chr(96)*3,prompts,re.S)
    urls=lambda text:set(re.findall(r"https://suno.com/song/[0-9a-f-]{36}",text))
    baseline=state["workflow"]["baseline"]
    guitar=[2,6,11,14,18,20];keys=[1,4,7,10,13,16,19];review=[3,5,8,9,12,15,17]
    bytrack={int(e["lineage_id"].split("-")[1]):e for e in state["prompt_register"]["entries"] if e.get("lineage_id","").startswith("TRK-")}
    checks={
      "new_user_requirement_registered":set(all_rids)=={"R%02d"%i for i in range(1,24)} and len(all_rids)==23
          and state["requirement_count"]==23 and state["music_goal_version"]==state["requirements_semantic_version"]=="0.5",
      "existing22_and_T_G_unchanged":sha("\n".join(old_rrows))==baseline["requirements_sha256"]
          and sha("\n".join(rows(criteria,r"^\| T\d{2} \|")))==baseline["T_sha256"]
          and sha("\n".join(rows(criteria,r"^\| G\d{2} ")))==baseline["G_sha256"],
      "source_is_user_not_invented_audio_analysis":state["feedback_records"][0]["id"]=="FB-000001"
          and state["feedback_records"][0]["assessment_actor"]=="USER"
          and state["feedback_records"][0]["output_ids"]=="NOT_SPECIFIED"
          and state["feedback_records"][0]["universal_music_claim"] is False,
      "current_scope_keyboard_main_guitar_main_stopped":policy["scope"]=="CURRENT_LOFI_PROFILE_ONLY"
          and policy["lead_family"]=="PIANO_OR_KEYBOARD" and policy["guitar_main_allowed"] is False
          and policy["guitar_main_prompt_tracks"]==guitar and policy["other_role_review_tracks"]==review,
      "support_not_globally_banned_and_not_frozen_song":policy["guitar_support"]=="NOT_DECIDED_NOT_GLOBALLY_BANNED"
          and policy["does_not_freeze_specific_melody_or_chord_progression"] is True,
      "all20_role_use_states_connected":sorted(bytrack)==list(range(1,21))
          and all(bytrack[n]["current_use_status"]=="DO_NOT_REUSE_GUITAR_MAIN" for n in guitar)
          and all(bytrack[n]["current_use_status"]=="HOLD_KEYBOARD_MAIN_REVIEW" for n in review)
          and all(bytrack[n]["current_use_status"]=="KEYBOARD_MAIN_ELIGIBLE_AUDIO_PENDING" for n in keys),
      "guitar_reuse_blocked_at_input_gate":all(preinput_gate(root,state,bytrack[n]["id"])["status"]=="DO_NOT_REUSE_GUITAR_MAIN" for n in guitar),
      "other_role_review_blocks_automatic_reuse":all(preinput_gate(root,state,bytrack[n]["id"])["status"]=="HOLD_KEYBOARD_MAIN_REVIEW" for n in review),
      "original42_input_blocks_preserved":current_prompts[:42]==old_prompts and len(old_prompts)==42,
      "original_design_file_unchanged":sha((root/"first_batch_designs.json").read_bytes())==state["workflow"]["latest_increment"]["pre_edit_hashes"]["first_batch_designs.json"],
      "all40_links_retained":urls(results)==urls(old_results) and len(urls(results))==40,
      "no_new_generation_or_cost":state["batch_generation"]["requests"]==old["batch_generation"]["requests"]
          and state["generation_attempts_count"]==old["generation_attempts_count"]==18
          and state["batch_generation"]["credit_decrease_observed"]==old["batch_generation"]["credit_decrease_observed"]==180,
      "historical_generation_verification_retained":old_report["passed"] and old_report["validator_version"]=="0.17.0",
      "no_false_output_acceptance_or_AI_listening":state["direct_audio_checks_count"]==0 and state["adopted_tracks_count"]==0
          and all(x["adoption_status"]=="NOT_ADOPTED" and x["audio_status"]=="NOT_ASSESSED" for x in designs["tracks"]),
      "entry_and_records_point_to_current_rule":all("R23" in (root/n).read_text(encoding="utf-8")
          for n in ["00_START_HERE.md","02_PRODUCTION_STANDARD.md","04_PRODUCTION_HISTORY.md","05_DECISIONS_AND_PROGRESS.md","18_PROMPT_REGISTER.md","19_BATCH_GENERATION.md"]),
      "fixed_fixture_hash_retained":sha((root/"workflow_cases.json").read_bytes())==baseline["cases_sha256"],
    }
    if state.get("opening_drum_revision"):
        rev=state["opening_drum_revision"]; pkgs=rev["packages"]
        flat=[v for x in pkgs for v in (x["style"],x["exclude"])]
        checks.update({
          "latest_feedback_scope_preserved":state["feedback_records"][-1]["id"]=="FB-000002" and state["feedback_records"][-1]["assessment_actor"]=="USER" and state["feedback_records"][-1]["output_ids"]=="NOT_SPECIFIED" and state["user_listening_feedback_count"]==len(state["feedback_records"])==2,
          "four_complete_drafts_match_register":len(pkgs)==4 and current_prompts[42:50]==flat and state["prompt_register"]["complete_prompt_count"]==(26 if state.get("simple_mode_test") else 25),
          "lengths_and_original_exclude_retained":all(len(x["style"])<=1000 and x["style_chars"]==len(x["style"]) and x["exclude"]==old["batch_generation"]["packages"][4]["exclude"] and len(x["exclude"])==308 and x["lyrics"]=="" for x in pkgs),
          "base_harmony_and_keyboard_main_retained":all("G minor: Gm7 4 bars, Ebmaj7 4." in x["style"] and "Felt upright piano remains the main voice" in x["style"] for x in pkgs),
          "four_opening_and_drum_families_differ":len({x["opening_family"] for x in pkgs})==len({x["drum_palette"] for x in pkgs})==4,
          "drafts_not_misreported_as_generated":all(x["status"]=="DRAFT_NOT_SUBMITTED" and x["actual_outputs"]==[] for x in pkgs) and rev["generation_status"]=="NOT_SUBMITTED",
          "draft_fingerprints_match":all(sha(x["style"])==x["style_sha256"] and sha(x["exclude"])==x["exclude_sha256"] for x in pkgs),
          "feedback_and_revision_linked":all("FB-000002" in (root/n).read_text(encoding="utf-8") for n in ["00_START_HERE.md","02_PRODUCTION_STANDARD.md","04_PRODUCTION_HISTORY.md","05_DECISIONS_AND_PROGRESS.md","18_PROMPT_REGISTER.md","20_OPENING_DRUM_REVISION.md"]),
        })
    if state.get("simple_mode_test"):
        simple=state["simple_mode_test"]
        checks.update({
          "simple_complete_input_matches_register":current_prompts[50:]==[simple["prompt"]] and sha(simple["prompt"])==simple["fingerprint_sha256"],
          "simple_within3000_and_not_submitted":len(simple["prompt"])==simple["total_chars"]<=3000 and simple["status"]=="DRAFT_NOT_SUBMITTED" and simple["actual_outputs"]==[],
          "simple_original28_exclusions_retained":simple["exclude"].split(", ")[:28]==old["batch_generation"]["packages"][4]["exclude"].split(", "),
          "simple_not_identical_to_old25_texts":simple["style"] not in current_prompts[:50] and simple["prompt"] not in current_prompts[:50],
        })
    fixtures=json.loads((root/"workflow_cases.json").read_text(encoding="utf-8"))
    docs={n:(root/n).read_text(encoding="utf-8") for n in CORE if n.endswith(".md")}
    cases=case_results(fixtures["cases"],docs,state,out)
    passed=all(checks.values()) and all(x["passed"] for x in cases)
    report={"validator_version":VERSION,"test_only":False,"scope":"User feedback/profile update, input reuse blocking and unchanged generation history",
        "passed":passed,"feedback_policy_checks":checks,
        "cases":[{"id":x["case_id"],"passed":x["passed"],"test_only":True} for x in cases],
        "new_requirement":"R23","actual_generation_this_update":0,
        "limitations":["Instrument-role classification is from stored designs, not new per-output audio judgments","Guitar accompaniment not automatically banned","Old input texts preserved as history, not automatically eligible for reuse"],
        "release_decision":"PASS_CURRENT_PROFILE_FEEDBACK_UPDATE" if passed else "REJECT"}
    payload=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    (root/"workflow_validation.json").write_text(payload,encoding="utf-8")
    (out/"lead_feedback.json").write_text(payload,encoding="utf-8")
    (out/"summary.json").write_text(payload,encoding="utf-8")
    print(json.dumps({"passed":passed,"checks":len(checks),"failed":[k for k,v in checks.items() if not v],"original_cases_passed":sum(x["passed"] for x in cases),"decision":report["release_decision"]},ensure_ascii=False))
    return 0 if passed else 1


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",default=".")
    parser.add_argument("--out",default="verification_runs/latest")
    parser.add_argument("--publication",action="store_true")
    parser.add_argument("--preinput-id",default=None)
    args=parser.parse_args()
    root=Path(args.root).resolve()
    out=Path(args.out)
    if not out.is_absolute():out=root/out
    out=out.resolve()
    if not out.is_relative_to(root):raise ValueError("Output must remain inside the project")
    out.mkdir(parents=True,exist_ok=True)
    state=json.loads((root/"project_state.json").read_text(encoding="utf-8"))
    if state.get("lead_instrument_policy") and not args.preinput_id:
        return validate_lead_feedback(root,state,out)
    if state.get("batch_generation",{}).get("status")=="COMPLETE_WAIT_USER_FEEDBACK" and not args.preinput_id:
        return validate_batch_release(root,state,out,args.publication)
    if args.preinput_id:
        gate=preinput_gate(root,state,args.preinput_id)
        print(json.dumps(gate,ensure_ascii=False))
        return 0 if gate["allowed"] else 2
    fixtures=json.loads((root/"workflow_cases.json").read_text(encoding="utf-8"))
    baseline=state["workflow"]["baseline"]
    docs={n:(root/n).read_text(encoding="utf-8") for n in CORE+["09_ORIGINAL_ANALYSIS.md","10_PRODUCT_CAPABILITIES.md","11_CASE_RESEARCH.md","12_MUSICAL_OPTIONS.md","13_EVIDENCE_AND_TEST_PLAN.md","14_REQUEST_INTAKE.md","15_REPEATABLE_PRODUCTION_WORKFLOW.md","p5_workflow_cases.json","16_FIRST_BATCH_DESIGNS.md","first_batch_designs.json","17_TRACK01_INPUT.md","18_PROMPT_REGISTER.md"] if n.endswith(".md")}
    checks=inspect(docs,state,fixtures,baseline,root,args.publication)
    cases=case_results(fixtures["cases"],docs,state,out)
    injected=mutations(docs,state,fixtures,baseline,root)
    baseline_checks=baseline_analysis_checks(docs)
    product_checks=product_record_checks(root,state)
    p2_checks=case_record_checks(root,state)
    p3_checks=musical_record_checks(root,state)
    p4_checks=comparison_plan_checks(root,state)
    intake_checks=intake_record_checks(root,state)
    p5_checks,p5_cases,p5_mutants=p5_procedure_checks(root,state,out)
    p6_checks,p6_mutants=p6_design_checks(root,state)
    pkg=state["track01_input"]
    fence=chr(96)*3
    original=docs["09_ORIGINAL_ANALYSIS.md"].split("### 회수 Exclude")[1].split(fence+"text\n",1)[1].split("\n"+fence,1)[0]
    input_checks={"full_exclude_preserved":pkg["exclude"]==original,
        "reported_style_limit":state["account_input_limits"]["advanced_style_max_chars"]==1000 and len(pkg["style"])<=1000 and pkg["style_limit_check"]["remaining"]==83,
        "observed_limits_scoped":state["account_input_limits"]["lyrics_max_chars"]==5000 and state["account_input_limits"]["exclude_max_chars"]==1000 and state["account_input_limits"]["source_id"]=="SRC-0089",
        "text_lengths_match":len(pkg["style"])==pkg["style_chars"]==917 and len(pkg["exclude"])==pkg["exclude_chars"]==308,
        "package_linked":pkg["style"] in docs["17_TRACK01_INPUT.md"] and pkg["exclude"] in docs["17_TRACK01_INPUT.md"],
        "no_false_account_commit":pkg["actual_controls"]["model"]=="v6-mini" and pkg["style_exact_in_form"] is True and pkg["exclude_exact_in_form"] is True and pkg["committed"] is False and pkg["execution_count"]==0}
    t2=state["track02_input"]
    t2_gate=preinput_gate(root,state,"PRM-000004")
    track02_checks={
      "complete_text_in_register":t2["style"] in docs["18_PROMPT_REGISTER.md"] and t2["exclude"] in docs["18_PROMPT_REGISTER.md"],
      "lengths_and_original_exclusions":len(t2["style"])==t2["style_chars"]==943 and len(t2["exclude"])==t2["exclude_chars"]==355
          and t2["exclude"].startswith(original+", "),
      "design_and_structure":all(x in t2["style"] for x in ["66 BPM","light swing","F6 for 3 bars","Bbmaj7 for 3","C6 for 2","frame-drum","No keyboards"])
          and "TRK-000002"==t2["track_id"],
      "preinput_review_current":t2_gate["allowed"],
      "generation_not_fabricated":t2["committed"] is False and t2["execution_count"]==0,
      "UI_exact_when_prepared":not t2["ui_draft_prepared"] or (t2["style_exact_in_form"] is True and t2["exclude_exact_in_form"] is True and t2["title_exact_in_form"] is True)
    }
    register_checks,gate_cases=prompt_register_checks(root,state)
    passed=all(track02_checks.values()) and all(register_checks.values()) and all(input_checks.values()) and all(c["passed"] for c in checks) and all(c["passed"] for c in cases) and all(m["rejected"] for m in injected) and all(baseline_checks.values()) and all(product_checks.values()) and all(p2_checks.values()) and all(p3_checks.values()) and all(p4_checks.values()) and all(intake_checks.values()) and all(p5_checks.values()) and all(p6_checks.values()) and all(m["rejected"] for m in p6_mutants)
    report={
        "validator_version":VERSION,"acceptance_id":baseline["acceptance_id"],
        "scope":"Document workflow checks and file-record dry-run only",
        "test_only":True,"independent_ai_execution":False,
        "network_audio_or_generation_performed":False,
        "passed":passed,"publication_identity_check":args.publication,
        "checks":checks,
        "baseline_analysis_checks":baseline_checks,
        "product_record_checks":product_checks,
        "p2_record_checks":p2_checks,
        "p3_record_checks":p3_checks,
        "p4_plan_checks":p4_checks,
        "intake_record_checks":intake_checks,
        "p5_procedure_checks":p5_checks,
        "p6_design_checks":p6_checks,
        "track01_input_checks":input_checks,
        "prompt_register_checks":register_checks,
        "track02_input_checks":track02_checks,
        "preinput_gate_cases":gate_cases,
        "p6_mutation_tests":p6_mutants,
        "p5_cases":[{"id":c["id"],"passed":c["passed"],"failures":c["failures"]} for c in p5_cases],
        "p5_mutation_tests":p5_mutants,
        "cases":[{"id":c["case_id"],"passed":c["passed"],"failures":c["failures"],
                  "record":str(out.relative_to(root)/(c["case_id"]+".json"))} for c in cases],
        "mutation_tests":injected,
        "acceptance_plan_sha256":baseline["cases_sha256"],
        "evidence_counts":{"cases":len(cases),"mutations":len(injected),"p5_cases":len(p5_cases),"p5_mutations":len(p5_mutants)},
        "remaining_input_limits":["Style/Exclude recovered from prior user quote; original screen not independently compared",
            "Original generation model/settings and approved linked reference audio not obtained",
            "Public product facts recorded; account input limits/ranges/compatibility remain unresolved",
            "P2 public cases have incomplete conditions; Q06/Q07 effects and long-listening comfort unresolved",
            "P3 D02 music choices are source-based design synthesis; actual Suno behavior and listening effects unverified",
            "P4 protocols are planned; complete actual inputs/account values/cost require commit before execution"],
        "limitations":["No separate model was evaluated",
            "Fixture observation flags are hypothetical, not real listening evidence",
            "Routing and record execution do not prove music generation quality"],
        "release_decision":("PASS_DECLARED_DOCUMENT_SCOPE" if args.publication else
            "CONTENT_AND_EXECUTION_PASS_PENDING_PUBLICATION") if passed else "REJECT"
    }
    payload=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    (root/"workflow_validation.json").write_text(payload,encoding="utf-8")
    (out/"summary.json").write_text(payload,encoding="utf-8")
    print(json.dumps({"passed":passed,"checks":len(checks),
        "cases_passed":sum(c["passed"] for c in cases),"cases":len(cases),
        "mutations_rejected":sum(m["rejected"] for m in injected),
        "decision":report["release_decision"],
        "failed_checks":[c["id"] for c in checks if not c["passed"]],
        "baseline_analysis_checks":baseline_checks,
        "product_record_checks":product_checks,
        "p2_record_checks":p2_checks,
        "p3_record_checks":p3_checks,
        "p4_plan_checks":p4_checks,
        "intake_record_checks":intake_checks,
        "p5_procedure_checks":p5_checks,
        "p6_design_checks":p6_checks,
        "track01_input_checks":input_checks,
        "prompt_register_checks":register_checks,
        "track02_input_checks":track02_checks,
        "preinput_gate_cases":gate_cases,
        "p6_mutation_tests":p6_mutants,
        "p5_cases":[{"id":c["id"],"passed":c["passed"],"failures":c["failures"]} for c in p5_cases],
        "p5_mutation_tests":p5_mutants,
        "failed_cases":[c["case_id"] for c in cases if not c["passed"]]},
        ensure_ascii=False))
    return 0 if passed else 1

if __name__=="__main__":
    sys.exit(main())
