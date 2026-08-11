# prompt-manager/main.py

prompts = [
    {
        "title": "Python 시작하기",
        "content": "Python의 기본 문법과 특징을 설명해주세요.",
        "category": "프로그래밍",
        "favorite": False
    },
    {
        "title": "Git 커밋 메시지 작성법",
        "content": "좋은 Git 커밋 메시지를 작성하는 규칙 5가지를 알려주세요.",
        "category": "개발도구",
        "favorite": True
    },
    {
        "title": "건강한 식단 추천",
        "content": "직장인을 위한 일주일치 건강한 저녁 식단을 짜주세요.",
        "category": "일상",
        "favorite": False
]

def add_prompt():
    print("\n--- 프롬프트 추가 ---")
    title = input("제목을 입력하세요: ").strip()
    if not title:
        print("오류: 제목은 필수입니다.")
        return
        
    content = input("내용을 입력하세요: ").strip()
    if not content:
        print("오류: 내용은 필수입니다.")
        return
        
    category = input("카테고리를 입력하세요 (기본값: 일반): ").strip()
    if not category:
        category = "일반"
        
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print("프롬프트가 성공적으로 추가되었습니다!")

def show_list():
    print("\n--- 프롬프트 목록 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
        
    for i, p in enumerate(prompts, 1):
        fav_star = "⭐" if p["favorite"] else "  "
        print(f"[{i}] {fav_star} [{p['category']}] {p['title']}")

def show_by_category():
    print("\n--- 카테고리별 보기 ---")
    categories = set(p['category'] for p in prompts)
    if not categories:
        print("등록된 카테고리가 없습니다.")
        return
        
    print(f"사용 가능한 카테고리: {', '.join(categories)}")
    target_category = input("조회할 카테고리를 입력하세요: ").strip()
    
    filtered_prompts = [(i, p) for i, p in enumerate(prompts, 1) if p['category'] == target_category]
    
    if not filtered_prompts:
        print(f"'{target_category}' 카테고리에 해당하는 프롬프트가 없습니다.")
        return
        
    for i, p in filtered_prompts:
        fav_star = "⭐" if p["favorite"] else "  "
        print(f"[{i}] {fav_star} [{p['category']}] {p['title']}")

def search_prompt():
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

def show_menu():
    print("\n" + "="*30)
    print("프롬프트 관리자")
    print("="*30)
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 카테고리별 보기")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 토글")
    print("7. 즐겨찾기 목록 보기")
    print("0. 종료")
    print("="*30)

def main():
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
        else:
            print("준비 중인 기능입니다.")

if __name__ == "__main__":
    main()
