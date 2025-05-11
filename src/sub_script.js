// ✅ 예시 대기 데이터
const waitData = {
    "16:00": 15,
    "17:00": 30,
    "18:00": 52
};

const latestCount = 56; // 현재 대기 인원 수 (예시)
const estimatedTime = Math.round(latestCount * 0.6); // 대기 시간 추정

// ✅ 차트 생성
const ctx = document.getElementById("waitChart").getContext("2d");
const chart = new Chart(ctx, {
    type: "bar",
    data: {
        labels: Object.keys(waitData),
        datasets: [{
            label: "대기 인원",
            data: Object.values(waitData),
            backgroundColor: "#4cd6b0",
            borderRadius: 6
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false },
            tooltip: {
                callbacks: {
                    label: function (context) {
                        return context.parsed.y + '명';
                    }
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    stepSize: 20,
                    callback: function (value) {
                        return value + '명';
                    }
                },
                grid: {
                    color: "#e0f0f5"
                }
            },
            x: {
                ticks: {
                    font: { size: 14 }
                },
                grid: { display: false }
            }
        }
    }
});

// ✅ 대기 정보 텍스트 갱신
document.getElementById("waitTime").innerText = `예상 시간: ${estimatedTime}분`;
document.getElementById("waitCount").innerText = `현재 대기 인원: ${latestCount}명`;

