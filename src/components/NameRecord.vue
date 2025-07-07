<template>
  <div style="max-width: 600px; margin: 0 auto;">
    <h1>選手登録</h1>

    <!-- 名前 -->
    <div>
      <label>名前</label><br />
      <input v-model="name" placeholder="名前を入力" />
    </div>

    <!-- 階級 -->
    <div>
      <label>階級</label><br />
      <select v-model="grade">
        <option disabled value="">階級を選択</option>
        <option>初級</option>
        <option>中級</option>
        <option>上級</option>
        <option>一般女子</option>
      </select>
    </div>

    <!-- 年齢 -->
    <div>
      <label>年齢</label><br />
      <select v-model="age">
        <option disabled value="">年齢を選択</option>
        <option v-for="n in 51" :key="n">{{ n + 9 }}</option> <!-- 10〜60歳 -->
      </select>
    </div>

    <!-- 性別 -->
    <div>
      <label>性別</label><br />
      <label><input type="radio" v-model="sex" value="男" checked /> 男</label>
      <label><input type="radio" v-model="sex" value="女" /> 女</label>
    </div>

    <!-- 道場 -->
    <div>
      <label>道場</label><br />
      <input v-model="affiliation" list="dojos" placeholder="道場名を入力" />
      <datalist id="dojos">
        <option value="赤龍館" />
        <option value="蒼空塾" />
        <option value="玄武館" />
        <option value="天翔会" />
      </datalist>
    </div>

    <!-- ボタン -->
    <div style="margin-top: 12px;">
      <button @click="registerName">登録</button>
      <button @click="loadNames">読み取り</button>
    </div>

    <!-- テーブル -->
    <table border="1" style="width: 100%; margin-top: 24px;">
      <thead>
        <tr>
          <th>No.</th><th>名前</th><th>階級</th><th>年齢</th><th>性別</th><th>道場</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in names" :key="index">
          <td>{{ index + 1 }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.grade }}</td>
          <td>{{ item.age }}</td>
          <td>{{ item.sex }}</td>
          <td>{{ item.affiliation }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const name = ref('')
const grade = ref('')
const age = ref('')
const sex = ref('')
const affiliation = ref('')
const names = ref([])
const isLoading = ref(false)
const error = ref('')

const loadNames = async () => {
  try {
    const res = await axios.get('/api/names')
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
  error.value = ''
  try {
    const res = await axios.post('/api/names', { 
      name: name.value.trim() 
      , grade: grade.value.trim()
      , age: age.value.trim()
      , sex: sex.value.trim()
      , affiliation: affiliation.value.trim()
    })  
    names.value.push(res.data.data)  
    name.value = ''
    grade.value = ''
    age.value =''
    sex.value = ''
    affiliation.value = ''
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
  if (!grade.value.trim()) {
    error.value = '階級を選択してください'
    return false
  }
  if (!age.value) {
    error.value = '年齢を選択してください'
    return false
  }
  if(!affiliation.value.trim()) {
    error.value = '道場名を入力してください'
    return false
  }
}

onMounted(() => {
  loadNames()
})
</script>