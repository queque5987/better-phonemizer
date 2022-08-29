function printName(text)  {
  // const name = document.getElementById('text').value;
  const name = text
  // const formData = new FormData();
  // var dictObject = {}
  // dictObject['transcription'] = 'Jack and Jill ran up the hill.';
  // const speakerInput = {
  //   transcription: 'Jack and Jill ran up the hill.'
  // }
  // formData.append('value', dictObject)
  var obj = new Object();
  obj.transcription = name;
  var jsonString = JSON.stringify(obj)
  fetch('https://better-phonemizer.herokuapp.com/inference', {
    method: 'POST',
    headers: {
    'Content-Type': 'application/json',
    },
    body: jsonString
  })
  .then((response) => response.json())
  .then((data) => console.log(data));
  // .then((result) => {
    // console.log('성공', result)
  // })
  document.getElementById("phoneme").innerText = data;
}
document.getElementById("transcription").addEventListener('change', function(){
  printName(this.value)
});


// // POST 메서드 구현 예제
// async function getData(url = 'https://better-phonemizer.herokuapp.com/inference', data = {"transcription", "Jack and Jill ran up the hill."}) {
//   // 옵션 기본 값은 *로 강조
//   const response = await fetch(url, {
//     method: 'GET', // *GET, POST, PUT, DELETE 등
//     mode: 'cors', // no-cors, *cors, same-origin
//     cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
//     credentials: 'same-origin', // include, *same-origin, omit
//     headers: {
//       'Content-Type': 'application/json',
//       // 'Content-Type': 'application/x-www-form-urlencoded',
//     },
//     redirect: 'follow', // manual, *follow, error
//     referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
//     body: JSON.stringify(data), // body의 데이터 유형은 반드시 "Content-Type" 헤더와 일치해야 함
//   });
//   return response.json(); // JSON 응답을 네이티브 JavaScript 객체로 파싱
// }
