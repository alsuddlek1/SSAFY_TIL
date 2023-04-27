const nums = [1, 2, 3, 4]

const squareFunc = function (nums) {
  return nums ** 2
}

const squarenums = nums.map(squareFunc)
console.log(squarenums)