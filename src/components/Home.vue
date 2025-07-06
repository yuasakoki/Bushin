<template>
    <header>
      <p>ホーム</p> 
      <p>こんにちは、ユーザーさん！</p> 
      <h1>武神会</h1>
      <h1>全日本空手形大会</h1> 
    </header>
    <body>
      <div class="home-button-list">
        <button @click="onChangePage('about')">一般女子</button>
        <button @click="onChangePage('about')">男子：上級</button>
        <button @click="onChangePage('about')">男子：中級</button>
        <button @click="onChangePage('about')">男子：初級</button>
        <button @click="onChangePage('about')">女子：上級</button>
        <button @click="onChangePage('about')">女子：中級</button>
        <button @click="onChangePage('about')">女子：初級</button>
      </div>
    </body>
</template>
<script setup>
defineProps(['onChangePage'])
</script>
<style>
#app {
  font-family: 'Arial';
  padding: 20px;
}
</style>