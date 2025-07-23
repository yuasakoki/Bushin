<template>
  <div class="container">
    <h1>審判員登録</h1>
    <div class="form-group">
      <label>名前</label>
      <input v-model="name" placeholder="名前を入力" />
    </div>
    <div class="form-group" v-for="(item, idx) in assignments" :key="idx">
      <label>{{ item.round }}</label>
      <select v-model="item.court_code">
        <option value="">未選択</option>
        <option>男子/初級/Aコート</option>
        <option>男子/初級/Bコート</option>
        <option>男子/初級/Cコート</option>
        <option>男子/初級/Dコート</option>
        <option>男子/初級/Eコート</option>
        <option>男子/初級/Fコート</option>
        <option>男子/初級/Gコート</option>
        <option>男子/初級/Hコート</option>
        <option>男子/初級/Iコート</option>
        <option>男子/中級/Aコート</option>
        <option>男子/中級/Bコート</option>
        <option>男子/中級/Cコート</option>
        <option>男子/中級/Dコート</option>
        <option>男子/中級/Eコート</option>
        <option>男子/中級/Fコート</option>
        <option>男子/中級/Gコート</option>
        <option>男子/中級/Hコート</option>
        <option>男子/中級/Iコート</option>
        <option>男子/上級/Aコート</option>
        <option>男子/上級/Bコート</option>
        <option>男子/上級/Cコート</option>
        <option>男子/上級/Dコート</option>
        <option>女子/初級/Aコート</option>
        <option>女子/初級/Bコート</option>
        <option>女子/初級/Cコート</option>
        <option>女子/初級/Dコート</option>
        <option>女子/初級/Eコート</option>
        <option>女子/初級/Fコート</option>
        <option>女子/初級/Gコート</option>
        <option>女子/初級/Hコート</option>
        <option>女子/初級/Iコート</option>
        <option>女子/中級/Aコート</option>
        <option>女子/中級/Bコート</option>
        <option>女子/中級/Cコート</option>
        <option>女子/中級/Dコート</option>
        <option>女子/中級/Eコート</option>
        <option>女子/中級/Fコート</option>
        <option>女子/中級/Gコート</option>
        <option>女子/中級/Hコート</option>
        <option>女子/中級/Iコート</option>
        <option>女子/上級/Aコート</option>
        <option>女子/上級/Bコート</option>
        <option>女子/上級/Cコート</option>
        <option>女子/上級/Dコート</option>
        <option>一般女子/Aコート</option>
        <option>一般女子/Bコート</option>
        <option>一般女子/Cコート</option>
        <option>一般女子/Dコート</option>
      </select>
      <label>役職</label>
      <select v-model="item.post_code">
        <option value=""></option>
        <option>主審</option>
        <option>副審</option>
        <option>記録</option>
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
            <th v-for="(item, idx) in assignments" :key="idx">{{ item.round }} 回目</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in names" :key="index">
            <td>{{ names.length - index }}</td>
            <td>{{ item.name }}</td>
            <td v-for="(round, idx) in item.assignments" :key="idx">
              {{ round.court_code ? `${round.court_code} / ${round.post_code}` : '-' }}
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
const assignments = ref([
  { round: '1', court_code: '', post_code: '' },
  { round: '2', court_code: '', post_code: '' },
  { round: '3', court_code: '', post_code: '' },
  { round: '4', court_code: '', post_code: '' },
  { round: '5', court_code: '', post_code: '' },
  { round: '6', court_code: '', post_code: '' }
])
const names = ref([])
const isLoading = ref(false)
const error = ref('')

const loadNames = async () => {
  try {
    const res = await axios.get('/api/referees')
    console.log("API Response:", res.data)

    if (res.data && Array.isArray(res.data)) {
      // APIレスポンスが配列の場合の処理
      names.value = res.data.map(referee => ({
        name: referee.name,
        assignments: referee.rounds.map(round => ({
          round: round.round,
          court_code: round.court_code,
          post_code: round.post_code
        }))
      }))
    } else if (res.data && res.data.data) {
      // APIレスポンスがオブジェクトで、dataプロパティを持つ場合の処理
      const refereeData = Array.isArray(res.data.data) ? res.data.data : [res.data.data]

      names.value = refereeData.map(referee => ({
        name: referee.name,
        assignments: (referee.rounds || []).map(round => ({
          round: round.round,
          court_code: round.court_code || '',
          post_code: round.post_code || ''
        }))
      }))
    } else {
      names.value = []
    }

    console.log("処理後のデータ:", names.value)
  } catch (e) {
    console.error('データ読み込みエラー:', e)
    alert('審判員データの読み込みに失敗しました')
    names.value = []
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
    // 審判員データの構築
    const refereeData = {
      name: name.value.trim(),
      assignments: assignments.value.map(gc => ({
        court_code: gc.court_code,
        post_code: gc.post_code,
        round: gc.round
      }))
    }

    // APIにPOSTリクエスト
    const res = await axios.post('/api/referees', refereeData)
    if (res.data?.data) {
      names.value.unshift(res.data.data)
    } else {
      console.warn("登録レスポンスに有効なデータが含まれていません:", res.data)
    }

    // フォームのリセット
    name.value = ''
    assignments.value.forEach(gc => {
      gc.court_code = ''
      gc.post_code = ''
    })

    console.log("登録後のデータ:", names.value)
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
  // setInterval(loadNames, 10000)
})
</script>