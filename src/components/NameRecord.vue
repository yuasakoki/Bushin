<template>
  <div>
    <h1>選手登録</h1>
    <input v-model="name" placeholder="名前を入力" />
    <button @click="registerName">登録</button>
    <button @click="loadNames">読み取り</button>

    <table border="1" style="margin-top: 20px; width: 500px;">
      <thead>
        <tr><th>No.</th><th>名前</th></tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in names" :key="index">
          <td>{{ index + 1 }}</td>
          <td>{{ item.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const name = ref('')
const names = ref([])
const isLoading = ref(false)
const error = ref('')

const loadNames = async () => {
  try {
    const res = await axios.get('http://localhost:5000/api/names')
    names.value = res.data.data
  } catch (e) {
    alert('名前一覧の読み込みに失敗しました')
  }
}

const registerName = async () => {
  // 値のチェック
  if (!name.value.trim()) {
    error.value = '名前を入力してください'
    alert(error.value)
    return
  }
  
  // 既存の名前と重複チェック
  isLoading.value = true
  error.value = ''
  try {
    const res = await axios.post('http://localhost:5000/api/names', { name: name.value.trim() })
    names.value.push(res.data.data)
    name.value = ''
  } catch (e) {
    console.error('名前の登録エラー:', e)
    error.value = '名前の登録に失敗しました'
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  loadNames()
})
</script>