<template>
  <div class="card">
    <!-- 넘겨받은 이미지가 고양이면 cat 빨강 -->
    <!-- 넘겨받은 이미지가 강아지면 dog 파랑 -->
    <!-- 조건부 클래스 바인딩 || :class={} -->
    <p
      :class="{
        'cat' : image.status === 'cat',
        'dog' : image.status === 'dog',
      }"
    > 
    {{image.status}} 
    </p>
    <img :src="image.url" >
  </div>
</template>

<script>
export default {
  name : 'AnimalCard',
  props: {
    image : Object
  }
}
</script>

<style>
.cat {
  color : red;
}

.dog{
  color : blue;
}

.card{
  width: 300px;
  height: 300px;
}

.card > img{
  width: 100%;
  height: 80%;
}
</style>