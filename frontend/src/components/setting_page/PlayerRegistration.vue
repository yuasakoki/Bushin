<template>
  <div
    class="min-h-screen flex flex-col items-center justify-center bg-white px-6 py-12 font-sawarabi min-w-[320px] text-red-700">

    <h1 class="text-5xl font-bold mb-12 border-b-4 border-red-300 pb-3 animate-fadeInDown">
      選手登録
    </h1>

    <div class="w-full max-w-md bg-white shadow-lg rounded-lg p-8 space-y-6 animate-slideUpSlow">
      <!-- 名前 -->
      <div>
        <label for="name" class="block mb-2 font-semibold text-red-700">名前</label>
        <input id="name" v-model="name" placeholder="名前を入力"
          class="w-full px-4 py-3 border border-red-400 rounded-md bg-red-700 text-white placeholder-red-300 focus:outline-none focus:ring-4 focus:ring-red-400 transition-all duration-300 hover:scale-105" />
      </div>
      <!-- 階級 -->
      <div>
        <label class="block mb-2 font-semibold text-red-700">階級</label>
        <select v-model="grade"
          class="w-full px-4 py-3 border border-red-400 rounded-md bg-red-700 text-white placeholder-red-300 focus:outline-none focus:ring-4 focus:ring-red-400 transition-all duration-300 hover:scale-105">
          <option disabled value="" class="text-red-300">階級を選択</option>
          <option class="text-black">初級</option>
          <option class="text-black">中級</option>
          <option class="text-black">上級</option>
          <option class="text-black">一般女子</option>
        </select>
      </div>

      <!-- 年齢 -->
      <div>
        <label class="block mb-2 font-semibold text-red-700">年齢</label>
        <select v-model="age"
          class="w-full px-4 py-3 border border-red-400 rounded-md bg-red-700 text-white placeholder-red-300 focus:outline-none focus:ring-4 focus:ring-red-400 transition-all duration-300 hover:scale-105">
          <option disabled value="" class="text-red-300">年齢を選択</option>
          <option v-for="n in 51" :key="n" class="text-black">{{ n + 9 }}</option>
        </select>
      </div>

      <!-- 性別 -->
      <div>
        <label class="block mb-2 font-semibold text-red-700">性別</label>
        <div class="flex gap-8">
          <label class="flex items-center gap-3 cursor-pointer select-none text-red-700">
            <input type="radio" v-model="gender" value="0" class="accent-red-600" />
            <span class="text-lg">男</span>
          </label>
          <label class="flex items-center gap-3 cursor-pointer select-none text-red-700">
            <input type="radio" v-model="gender" value="1" class="accent-red-600" />
            <span class="text-lg">女</span>
          </label>
        </div>
      </div>

      <!-- 道場 -->
      <div>
        <label class="block mb-2 font-semibold text-red-700">道場</label>
        <input v-model="affiliation" list="dojos" placeholder="道場名を入力"
          class="w-full px-4 py-3 border border-red-400 rounded-md bg-red-700 text-white placeholder-red-300 focus:outline-none focus:ring-4 focus:ring-red-400 transition-all duration-300 hover:scale-105" />
        <datalist id="dojos">
          <option value="赤龍館" />
          <option value="蒼空塾" />
          <option value="玄武館" />
          <option value="天翔会" />
        </datalist>
      </div>

      <!-- ボタン -->
      <div class="flex justify-between mt-8">
        <button @click="registerName"
          class="bg-red-600 hover:bg-red-700 text-white font-bold py-3 px-8 rounded-lg shadow-lg transform transition-transform duration-300 hover:scale-110 active:scale-95">
          登録
        </button>
        <button @click="loadNames"
          class="bg-white border-2 border-red-600 text-red-600 font-bold py-3 px-8 rounded-lg shadow-lg hover:bg-red-50 transform transition-transform duration-300 hover:scale-110 active:scale-95">
          読み取り
        </button>
      </div>
    </div>

    <!-- テーブル -->
    <div class="w-full max-w-6xl mt-16 overflow-x-auto shadow-lg rounded-lg bg-white animate-fadeInUp">
      <table class="min-w-full border-collapse table-auto">
        <thead class="bg-red-100 border-b-2 border-red-300">
          <tr>
            <th class="py-4 px-6 text-sm font-semibold text-red-700">No.</th>
            <th class="py-4 px-6 text-sm font-semibold text-red-700">名前</th>
            <th class="py-4 px-6 text-sm font-semibold text-red-700">階級</th>
            <th class="py-4 px-6 text-sm font-semibold text-red-700">年齢</th>
            <th class="py-4 px-6 text-sm font-semibold text-red-700">性別</th>
            <th class="py-4 px-6 text-sm font-semibold text-red-700">道場</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in names" :key="index"
            class="border-b border-gray-200 hover:bg-red-50 transition-colors animate-fadeInUp">
            <td class="py-3 px-6 text-sm text-red-700">{{ names.length - index }}</td>
            <td class="py-3 px-6 text-sm text-red-700">{{ item.name }}</td>
            <td class="py-3 px-6 text-sm text-red-700">{{ item.grade }}</td>
            <td class="py-3 px-6 text-sm text-red-700">{{ item.age }}</td>
            <td class="py-3 px-6 text-sm text-red-700">{{ item.gender === '0' ? '男' : '女' }}</td>
            <td class="py-3 px-6 text-sm text-red-700">{{ item.affiliation }}</td>
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
const grade = ref('')
const age = ref('')
const gender = ref('0') // デフォルトは男性
const affiliation = ref('')
const names = ref([])
const isLoading = ref(false)
const error = ref('')

const loadNames = async () => {
  try {
    const res = await axios.get('/api/names')
    names.value = Object.values(res.data.data || {}) // res.data.dataがnull/undefinedの場合に備えて空オブジェクトをデフォルトにする
    console.log("Names loaded:", names.value); // デバッグ用にログ出力
  } catch (e) {
    alert('名前一覧の読み込みに失敗しました')
    console.error('名前一覧の読み込みエラー:', e); // エラー詳細をコンソールに出力
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
    const res = await axios.post('/api/names', {
      name: name.value.trim()
      , grade: grade.value.trim()
      , age: age.value.trim()
      , gender: gender.value.trim()
      , affiliation: affiliation.value.trim()
    })
    setTimeout(loadNames, 500); // 読込が早すぎるため0.5秒待機
    if (res.data?.data) {
      names.value.push(res.data.data)
    } else {
      console.warn("登録レスポンスに有効なデータが含まれていません:", res.data)
    }
    name.value = ''
    grade.value = ''
    age.value = ''
    affiliation.value = ''
  } catch (e) {
    console.error('名前の登録エラー:', e)
    error.value = '名前の登録に失敗しました'
  } finally {
    isLoading.value = false
  }
}

const chekcvalue = () => {
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
  if (!affiliation.value.trim()) {
    error.value = '道場名を入力してください'
    return false
  }
  return true
}

// onMounted(() => {
//   loadNames()
//   setInterval(loadNames, 10000); // 10秒ごとに取得
// })
</script>