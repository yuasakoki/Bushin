<template>
  <h1>管理者メニュー</h1>
  <div id="settings">
    <button @click="onChangePage('refereeRegistration')">審判員</button><br>
    <button @click="onChangePage('playerRegistration')">選手登録</button><br>
    <button @click="onChangePage('refereeRegistration')">審判員登録</button>
  </div>
</template>
<script setup>
defineProps(['onChangePage'])
</script>