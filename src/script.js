// 🔸 검색 대상 데이터
const items = ["성심당"]; // 검색 대상으로 사용할 데이터 배열

// 🔸 검색 함수
function handleSearch() {
    const input = document.getElementById("searchInput").value.trim(); // 입력창의 텍스트 추출 및 공백 제거
    const result = document.getElementById("result"); // 결과 출력 영역

    // 입력값이 비어있을 경우 안내 문구 출력
    if (input === "") {
        result.innerText = "검색어를 입력해주세요.";
        return;
    }

    // 입력된 텍스트를 포함하는 항목을 필터링
    const matched = items.filter(item => item.includes(input));

    if (matched.length === 0) {
        // 일치 항목이 없을 경우 메시지 출력
        result.innerText = `"${input}"에 대한 결과가 없습니다.`;  // 수정: 템플릿 리터럴 사용
    } else {
        // 검색 결과가 있을 경우 HTML로 결과 표시
        result.innerHTML = `
            <strong>"${input}" 검색 결과:</strong><br><br>
            <a href="sub_index.html">• 성심당</a>
        `;
    }
}

// 🔸 엔터 키 이벤트 등록
document.addEventListener("DOMContentLoaded", function () {
    // 페이지가 로드된 후 검색창에 이벤트 리스너 부착
    document.getElementById("searchInput").addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            handleSearch(); // 엔터 키 누를 경우 검색 실행
        }
    });
});