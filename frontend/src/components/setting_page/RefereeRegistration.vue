<template>
  <div class="container">
    <h1>審判員登録</h1>
    <div class="form-group">
      <label>名前</label><br />
      <input v-model="name" placeholder="名前を入力" />
    </div>
    <div class="form-group" v-for="(item, idx) in gradeCourtList" :key="idx">
      <label>{{ item.label }} 階級</label>
      <select v-model="item.grade">
        <option value="">未選択</option>
        <option>初級</option>
        <option>中級</option>
        <option>上級</option>
        <option>一般女子</option>
      </select>
      <label style="margin-left:1em;">コート</label>
      <select v-model="item.court">
        <option value="">未選択</option>
        <option>A</option>
        <option>B</option>
        <option>C</option>
        <option>D</option>
        <option>E</option>
        <option>F</option>
        <option>G</option>
        <option>H</option>
      </select>
    </div>
    <div class="form-group">
      <button @click="registerName">登録</button>
      <button @click="loadNames">読み取り</button>
    </div>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>No.</th>
            <th>名前</th>
            <th v-for="(item, idx) in gradeCourtList" :key="idx">{{ item.label }} 階級</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in names" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ item.name }}</td>
            <td v-for="(gc, idx) in item.gradeCourts || []" :key="idx">
              {{ gc.grade }} / {{ gc.court }}
            </td>
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
const gradeCourtList = ref([
  { label: '1', grade: '', court: '' },
  { label: '2', grade: '', court: '' },
  { label: '3', grade: '', court: '' },
  { label: '4', grade: '', court: '' },
  { label: '5', grade: '', court: '' },
  { label: '6', grade: '', court: '' }
])
const names = ref([])
const isLoading = ref(false)
const error = ref('')

const loadNames = async () => {
  try {
    const res = await axios.get('/api/Referee')
    names.value = res.data.data
  } catch (e) {
    alert('名前一覧の読み込みに失敗しました')
    console.error(e)
  }
}

const registerName = async () => {
  error.value = ''
  if (!name.value.trim()) {
    alert('名前を入力してください')
    return
  }
  
  isLoading.value = true
  try {
    const res = await axios.post('/api/Referee', {
      name: name.value.trim(),
      gradeCourts: gradeCourtList.value.map(gc => ({ grade: gc.grade, court: gc.court }))
    })
    names.value.push(res.data.data)
    name.value = ''
    gradeCourtList.value.forEach(gc => { gc.grade = ''; gc.court = '' })
  } catch (e) {
    alert('登録失敗: ' + (e.response?.data?.error || e.message))
    console.error('名前の登録エラー:', e)
    error.value = '名前の登録に失敗しました'
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  loadNames()
  setInterval(loadNames, 10000)
})
</script>