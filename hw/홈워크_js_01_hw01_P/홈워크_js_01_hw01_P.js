// 1번
const nums = [1,2,3,4,5,6,7,8]


console.log('1번 출력 결과')

for (let i = 0; i < nums.length; i++) {
  console.log('nums[' + i + ']: ' + nums[i])
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

// 2번
console.log('2번 출력 결과')
for (const num in nums) {
  console.log(nums[num], typeof nums[num])

}

console.log('2번 출력 결과-2') 
for (const num of nums) {
  console.log(num, typeof num)
}
