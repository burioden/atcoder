const judgeStatusLabel = document.querySelector("#judge-status span");
let judgeStatus = judgeStatusLabel.textContent;

function changeColor() {
    if (judgeStatus == "AC") {
        if (judgeStatusLabel.style.backgroundColor == "rgb(92, 184, 92)") {
            judgeStatusLabel.style.backgroundColor = "yellow";
        } else {
            judgeStatusLabel.style.backgroundColor = "rgb(92, 184, 92)";
        }
    } else if (judgeStatus == "TLE") {
        console.log(judgeStatusLabel.style.backgroundColor);
    }
}

setInterval(changeColor, 500);




// function changeColor() {
//     if (judgeStatusBgColor == "#5cb85c") {
//         judgeStatusBgColor = "yellow";
//     } else if (judgeStatusBgColor == "#f0ad4e") {
//         judgeStatusBgColor = "blue";
//     } else if (judgeStatusBgColor == "yellow") {
//         judgeStatusBgColor = "#5cb85c";
//     } else if (judgeStatusBgColor == "blue") {
//         judgeStatusBgColor = "#f0ad4e";
//     }
// }