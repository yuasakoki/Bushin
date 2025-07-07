<template>
  <div class="container">
    <h1>審判員登録</h1>

    <!-- 名前 -->
    <div class="form-group">
      <label>名前</label><br />
      <input v-model="name" placeholder="名前を入力" />
    </div>

    <!-- ボタン -->
    <div class="form-group">
      <button @click="registerName">登録</button>
      <button @click="loadNames">読み取り</button>
    </div>

    <!-- テーブル -->
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>No.</th><th>名前</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in names" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ item.name }}</td>
          </tr>
        </tbody>
      </table>
    </div>
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
    const res = await axios.get('/api/Referee')
    console.log(res.data) // ← ここでレスポンスを確認
    names.value = res.data.data
  } catch (e) {
    alert('名前一覧の読み込みに失敗しました')
  }
}

const registerName = async () => {
  error.value = ''
  // 値のチェック
  if (!chekcvalue()) {
    alert(error.value)
    return
  }
  
  // 既存の名前と重複チェック
  isLoading.value = true
  try {
    const res = await axios.post('/api/Referee', { 
      name: name.value.trim() 
    })  
    names.value.push(res.data.data)  
    name.value = ''
  } catch (e) {
    console.error('名前の登録エラー:', e)
    error.value = '名前の登録に失敗しました'
  } finally {
    isLoading.value = false
  }
}

const chekcvalue = () =>{
  if (!name.value.trim()) {
    error.value = '名前を入力してください'
    return false
  }
}

onMounted(() => {
  loadNames()
})
</script>