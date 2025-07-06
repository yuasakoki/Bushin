<template>
  <div>
    <h1>選手登録</h1><input v-model="name" placeholder="名前を入力" />

    <!-- 階級: コンボボックス -->
    <select v-model="grade">
      <option disabled value="">階級を選択</option>
      <option>初級</option>
      <option>中級</option>
      <option>上級</option>
      <option>一般女子</option>
    </select>

    <!-- 年齢: コンボボックス（10〜60歳） -->
    <select v-model="age">
      <option disabled value="">年齢を選択</option>
      <option v-for="n in 51" :key="n">{{ n + 1 }}</option>
    </select>

    <!-- 性別: ラジオボタン -->
    <div>
      <label><input type="radio" v-model="sex" value="男" /> 男</label>
      <label><input type="radio" v-model="sex" value="女" /> 女</label>
    </div>

    <!-- 道場: 入力付きコンボボックス（datalist） -->
    <input v-model="affiliation" list="dojos" placeholder="道場名を入力" />
    <datalist id="dojos">
      <option value="赤龍館" />
      <option value="蒼空塾" />
      <option value="玄武館" />
      <option value="天翔会" />
    </datalist>
    <br />
    <button @click="registerName">登録</button>
    <button @click="loadNames">読み取り</button>

    <table border="1" style="width: 700px;">
      <thead>
        <tr><th>No.</th><th>名前</th><th>階級</th><th>年齢</th><th>性別</th><th>道場</th></tr>
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
    const res = await axios.post('http://localhost:5000/api/names', { 
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

onMounted(() => {
  loadNames()
})
</script>