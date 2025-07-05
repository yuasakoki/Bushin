<template>
  <div>
    <h2>これは別ページです（URLはそのまま）</h2>
    <button @click="show = !show">
      {{ show ? '非表示にする' : '表示する' }}
    </button>

    <p v-if="show">こんにちは、こーきくん！これはv-ifで表示されているテキストです。</p>
    <p v-else>こんにちは、こーきくん！これはv-ifで非表示になっているテキストです。</p>
  
  </div>
</template>
<script setup>
import { ref } from 'vue'
const show = ref(true)
</script>