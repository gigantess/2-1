# prompt-manager/main.py

import json
import os
import sys

DATA_FILE = 'prompts.json'

def load_prompts():
    """prompts.json 파일에서 데이터를 로드하고, 조회수(views) 속성을 초기화합니다."""
    global prompts
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                prompts = json.load(f)
        except json.JSONDecodeError:
            prompts = []
        for p in prompts:
            if 'views' not in p:
                p['views'] = 0
    else:
        prompts = [
            {
                "title": "회의록 요약 코치 (Few-shot & Persona)",
                "content": "[역할(Persona)]\n너는 20년 경력의 'SW 품질 컨설팅 전문 프로젝트 매니저' 역할을 수행하는 AI 업무 코치야.\n\n[목표(Objective)]\n제공되는 회의 녹취록이나 메모를 분석하여, 명확한 결정사항과 Action Item을 도출하고 사내 공유용 템플릿에 맞춰 요약본을 작성한다.\n\n[작업 원칙 및 안전장치]\n1. 추측성 표현을 절대 금지하며, 원문에 없는 내용은 절대 지어내지 않는다.\n2. 사실/수치/정책/일정과 관련된 내용 중 근거가 부족하거나 모호한 부분은 임의로 작성하지 말고 반드시 \"확인 필요\" 항목으로 별도 분류한다.",
                "category": "업무자동화",
                "favorite": True,
                "views": 0
            },
            {
                "title": "시네마틱 영상 생성 (Google Veo 3.1)",
                "content": "[Scene 01: 무채색의 일상]\nCinematic bust shot of a 20-year-old Asian Gen Z youth with short black hair, wearing a black oversized streetwear hoodie, standing in a dull, monochrome gray subway station. The youth is bored and expressionless, blinks slowly, and lets out a subtle sigh, dropping their shoulders slightly. The camera has a very slight handheld shake. Flat, diffuse lighting, muted monochrome color palette, highly detailed, photorealistic, shot on 35mm lens.",
                "category": "멀티미디어",
                "favorite": True,
                "views": 0
            },
            {
                "title": "고객 피드백 실시간 JSON 분석",
                "content": "당신은 고객의 피드백을 실시간으로 분석하는 전문 AI 어시스턴트입니다.\n사용자가 제공한 피드백 텍스트를 분석하여 아래 세 가지 항목을 도출하고, 반드시 유효한 JSON 형식으로만 응답해 주세요.\n\n1. summary: 피드백의 핵심 내용을 파악하여 1문장으로 요약\n2. sentiment: 감정 판별 (Positive / Negative / Neutral)\n3. urgency: 긴급도 판별 (High / Low)",
                "category": "데이터분석",
                "favorite": False,
                "views": 0
            },
            {
                "title": "IT 뉴스 기사 자동 요약 및 분류",
                "content": "당신은 최신 IT/기술 트렌드 뉴스 기사를 분석하고 요약하는 전문 AI 에디터입니다.\n입력된 뉴스 기사의 제목과 본문을 분석하여 핵심 내용을 3줄(문자열 배열)로 요약하고, 카테고리(AI / Dev/Cloud)를 분류해 주세요. 결과는 반드시 유효한 JSON 형식으로만 반환해야 합니다.",
                "category": "데이터분석",
                "favorite": False,
                "views": 0
            }
        ]

def save_prompts():
    """현재 메모리의 prompts 리스트를 DATA_FILE에 JSON 형식으로 영속화(저장)합니다."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(prompts, f, ensure_ascii=False, indent=4)

def add_prompt():
    """사용자로부터 프롬프트 제목, 내용, 카테고리를 입력받아 목록에 추가하고 저장합니다."""
    print("\n--- 프롬프트 추가 ---")
    title = input("제목을 입력하세요: ").strip()
    if not title:
        print("오류: 제목은 필수입니다.")
        return
    if len(title) > 50:
        print("오류: 제목은 50자를 초과할 수 없습니다.")
        return
        
    # 중복 제목 검사 및 자동 접미사 부여 (_1, _2...)
    original_title = title
    suffix = 1
    while any(p['title'] == title for p in prompts):
        title = f"{original_title}_{suffix}"
        suffix += 1
    if title != original_title:
        print(f"중복된 제목이 존재하여 '{title}'(으)로 변경되었습니다.")
        
    content = input("내용을 입력하세요: ").strip()
    if not content:
        print("오류: 내용은 필수입니다.")
        return
        
    category = input("카테고리를 입력하세요 (기본값: 일반): ").strip()
    if not category:
        category = "일반"
    
    # 카테고리 정규화 (모두 대문자로 변환하여 유사명 방지)
    category = category.upper()
        
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "views": 0
    })
    save_prompts()
    print("프롬프트가 성공적으로 추가되었습니다!")

def show_list():
    """전체 프롬프트 목록을 번호, 즐겨찾기 상태, 카테고리, 제목과 함께 출력합니다."""
    print("\n--- 프롬프트 목록 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
        
    for i, p in enumerate(prompts, 1):
        fav_star = "⭐" if p["favorite"] else "  "
        print(f"[{i}] {fav_star} [{p['category']}] {p['title']}")

def show_by_category():
    """저장된 전체 카테고리 목록을 보여주고, 사용자가 선택한 카테고리의 프롬프트만 출력합니다."""
    print("\n--- 카테고리별 보기 ---")
    categories = sorted(set(p['category'] for p in prompts))
    if not categories:
        print("등록된 카테고리가 없습니다.")
        return
        
    print("사용 가능한 카테고리:")
    for i, cat in enumerate(categories, 1):
        print(f"[{i}] {cat}")
        
    cat_choice = input("조회할 카테고리 번호 또는 이름을 입력하세요: ").strip()
    
    # 인덱스 번호로 입력한 경우
    if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
        target_category = categories[int(cat_choice) - 1]
    else:
        # 이름으로 입력한 경우
        target_category = cat_choice.upper()
    
    filtered_prompts = [(i, p) for i, p in enumerate(prompts, 1) if p['category'] == target_category]
    
    if not filtered_prompts:
        print(f"'{target_category}' 카테고리에 해당하는 프롬프트가 없습니다.")
        return
        
    for i, p in filtered_prompts:
        fav_star = "⭐" if p["favorite"] else "  "
        print(f"[{i}] {fav_star} [{p['category']}] {p['title']}")

def search_prompt():
    """입력받은 키워드가 제목이나 내용에 포함된(부분 문자열 검색) 프롬프트를 찾아 출력합니다."""
    print("\n--- 프롬프트 검색 ---")
    keyword = input("검색할 키워드를 입력하세요: ").strip().lower()
    
    if not keyword:
        print("검색어를 입력해야 합니다.")
        return
        
    filtered_prompts = [
        (i, p) for i, p in enumerate(prompts, 1) 
        if keyword in p['title'].lower() or keyword in p['content'].lower()
    ]
    
    if not filtered_prompts:
        print(f"'{keyword}'에 해당하는 프롬프트가 없습니다.")
        return
        
    for i, p in filtered_prompts:
        fav_star = "⭐" if p["favorite"] else "  "
        print(f"[{i}] {fav_star} [{p['category']}] {p['title']}")

def show_detail():
    """선택한 번호의 프롬프트 상세 내용(제목, 카테고리, 내용)을 출력하고 조회수를 1 증가시킵니다."""
    print("\n--- 프롬프트 상세 보기 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    show_list()
    try:
        idx = int(input("상세보기 할 프롬프트 번호를 입력하세요: ")) - 1
        if 0 <= idx < len(prompts):
            p = prompts[idx]
            p['views'] += 1
            save_prompts()
            print("-" * 30)
            print(f"제목: {p['title']}")
            print(f"카테고리: {p['category']}")
            print(f"조회수: {p['views']} | 즐겨찾기: {'⭐' if p['favorite'] else 'X'}")
            print("-" * 30)
            print(p['content'])
            print("-" * 30)
        else:
            print("오류: 목록에 없는 번호입니다.")
    except ValueError:
        print("오류: 리스트에 있는 유효한 메뉴 번호를 정확히 입력해 주세요.")

def toggle_favorite():
    """선택한 번호의 프롬프트 즐겨찾기 상태(True/False)를 반전시킵니다."""
    print("\n--- 즐겨찾기 추가/삭제 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    show_list()
    try:
        idx = int(input("즐겨찾기를 설정/해제할 프롬프트 번호를 입력하세요: ")) - 1
        if 0 <= idx < len(prompts):
            confirm = input(f"'{prompts[idx]['title']}' 프롬프트의 즐겨찾기 상태를 변경하시겠습니까? (y/n): ").strip().lower()
            if confirm == 'y':
                prompts[idx]['favorite'] = not prompts[idx]['favorite']
                save_prompts()
                status = "설정" if prompts[idx]['favorite'] else "해제"
                print(f"'{prompts[idx]['title']}' 즐겨찾기가 {status}되었습니다.")
            else:
                print("즐겨찾기 상태 변경이 취소되었습니다.")
        else:
            print("오류: 목록에 없는 번호입니다.")
    except ValueError:
        print("오류: 리스트에 있는 유효한 메뉴 번호를 정확히 입력해 주세요.")

def show_favorites():
    """즐겨찾기(favorite == True)로 설정된 프롬프트들만 모아서 출력합니다."""
    print("\n--- 즐겨찾기 목록 ---")
    favorites = [(i, p) for i, p in enumerate(prompts, 1) if p['favorite']]
    
    if not favorites:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return
        
    for i, p in favorites:
        print(f"[{i}] ⭐ [{p['category']}] {p['title']}")

def export_to_markdown():
    """카테고리별로 프롬프트들을 그룹화하여, 카테고리명.md 파일로 내보냅니다."""
    categories = set(p['category'] for p in prompts)
    for cat in categories:
        filename = f"{cat}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# {cat} 프롬프트 모음\n\n")
            cat_prompts = [p for p in prompts if p['category'] == cat]
            for p in cat_prompts:
                fav = "⭐" if p['favorite'] else ""
                f.write(f"## {p['title']} {fav}\n\n")
                f.write(f"{p['content']}\n\n")
                f.write("---\n\n")
    print("마크다운 파일 내보내기가 완료되었습니다.")

def top_views():
    """조회수(views)가 가장 높은 상위 5개의 프롬프트를 내림차순으로 출력합니다."""
    print("\n--- 인기 프롬프트 (조회수순) ---")
    sorted_prompts = sorted(enumerate(prompts, 1), key=lambda x: x[1]['views'], reverse=True)
    if not sorted_prompts:
        print("등록된 프롬프트가 없습니다.")
        return
        
    for i, p in sorted_prompts[:5]:  # Top 5
        print(f"[{i}] 조회수: {p['views']} | [{p['category']}] {p['title']}")

def edit_prompt():
    """선택한 프롬프트의 제목, 내용, 카테고리를 새 값으로 수정합니다. (엔터 시 기존 값 유지)"""
    print("\n--- 프롬프트 수정 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    show_list()
    try:
        idx = int(input("수정할 프롬프트 번호를 입력하세요: ")) - 1
        if 0 <= idx < len(prompts):
            p = prompts[idx]
            print(f"현재 제목: {p['title']}")
            title = input("새 제목 (엔터 시 유지): ").strip()
            if title: p['title'] = title
            
            print(f"현재 내용: {p['content']}")
            content = input("새 내용 (엔터 시 유지): ").strip()
            if content: p['content'] = content
            
            print(f"현재 카테고리: {p['category']}")
            category = input("새 카테고리 (엔터 시 유지): ").strip()
            if category: p['category'] = category.upper()
            
            save_prompts()
            print("프롬프트가 수정되었습니다.")
        else:
            print("오류: 목록에 없는 번호입니다.")
    except ValueError:
        print("오류: 리스트에 있는 유효한 메뉴 번호를 정확히 입력해 주세요.")

def delete_prompt():
    """선택한 프롬프트를 삭제합니다. 삭제 전 사용자에게 최종 확인을 받습니다."""
    print("\n--- 프롬프트 삭제 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    show_list()
    try:
        idx = int(input("삭제할 프롬프트 번호를 입력하세요: ")) - 1
        if 0 <= idx < len(prompts):
            confirm = input(f"'{prompts[idx]['title']}' 프롬프트를 정말 삭제하시겠습니까? (y/n): ").strip().lower()
            if confirm == 'y':
                del prompts[idx]
                save_prompts()
                print("프롬프트가 삭제되었습니다.")
            else:
                print("삭제가 취소되었습니다.")
        else:
            print("오류: 목록에 없는 번호입니다.")
    except ValueError:
        print("오류: 리스트에 있는 유효한 메뉴 번호를 정확히 입력해 주세요.")

def show_menu():
    """메인 메뉴 선택지를 터미널에 출력합니다."""
    print("\n" + "="*30)
    print("프롬프트 관리자")
    print("="*30)
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 카테고리별 보기")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 추가/삭제")
    print("7. 즐겨찾기 목록 보기")
    print("8. Markdown 내보내기")
    print("9. 인기 프롬프트 (조회수순)")
    print("10. 프롬프트 수정")
    print("11. 프롬프트 삭제")
    print("0. 종료")
    print("="*30)

def main():
    """프로그램의 메인 진입점. 데이터를 로드하고 무한 루프를 통해 메뉴 선택을 처리합니다."""
    load_prompts()
    try:
        while True:
            show_menu()
            choice = input("메뉴를 선택하세요: ")
            
            if choice == '0':
                print("프로그램을 종료합니다.")
                break
            elif choice == '1':
                add_prompt()
            elif choice == '2':
                show_list()
            elif choice == '3':
                show_by_category()
            elif choice == '4':
                search_prompt()
            elif choice == '5':
                show_detail()
            elif choice == '6':
                toggle_favorite()
            elif choice == '7':
                show_favorites()
            elif choice == '8':
                export_to_markdown()
            elif choice == '9':
                top_views()
            elif choice == '10':
                edit_prompt()
            elif choice == '11':
                delete_prompt()
            else:
                print("준비 중인 기능입니다.")
    except KeyboardInterrupt:
        print("\n\n안전하게 프로그램을 종료합니다. (데이터 자동 저장)")
        save_prompts()
        sys.exit(0)

if __name__ == "__main__":
    main()
