words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

function palindrome(word) {
    // word가 회문인지 아닌지 판별
    var new_word = ""; //함수의 중괄호 내부를 가르키기 때문에 var
    for (var i = word.length-1; i>=0; i--){
      new_word += word[i];
    }
      if (word === new_word){
        return new_word
      }
      else{
        return 'false'
      }
    }
    
for (const word of words) {
  console.log(palindrome(word))
}

// 출력 예시
// true
// true
// true
// false
// false
// false
