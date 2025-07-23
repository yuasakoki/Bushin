<template>
  <div
    class="min-h-screen flex flex-col items-center justify-center bg-white px-6 py-12 font-sawarabi min-w-[320px] text-red-700">

    <h1 class="text-5xl font-bold mb-12 border-b-4 border-red-300 pb-3 animate-fadeInDown">
      選手登録
    </h1>

    <div class="w-full max-w-md bg-white shadow-lg rounded-lg p-8 space-y-6 animate-slideUpSlow">
      <!-- 名前 -->
      <div>
        <label for="name" class="block mb-2 font-semibold text-red-700">選手名</label>
        <input id="name" v-model="name" placeholder="選手名を入力"
          class="w-full px-4 py-3 border border-red-400 rounded-md bg-red-700 text-white placeholder-red-300 focus:outline-none focus:ring-4 focus:ring-red-400 transition-all duration-300 hover:scale-105" />
      </div>
      <!-- 階級 -->
      <div>
        <label class="block mb-2 font-semibold text-red-700">段・級</label>
        <select v-model="grade"
          class="w-full px-4 py-3 border border-red-400 rounded-md bg-red-700 text-white placeholder-red-300 focus:outline-none focus:ring-4 focus:ring-red-400 transition-all duration-300 hover:scale-105">
          <option disabled value="" class="text-red-300">段・級を選択</option>
          <option class="text-black">8級</option>
          <option class="text-black">7級</option>
          <option class="text-black">6級</option>
          <option class="text-black">5級</option>
          <option class="text-black">4級</option>
          <option class="text-black">3級</option>
          <option class="text-black">2級</option>
          <option class="text-black">1級</option>
          <option class="text-black">初段</option>
          <option class="text-black">弐段</option>
          <option class="text-black">参段</option>
        </select>
      </div>

      <!-- 年齢 -->
      <div>
        <label class="block mb-2 font-semibold text-red-700">年齢</label>
        <select v-model="age"
          class="w-full px-4 py-3 border border-red-400 rounded-md bg-red-700 text-white placeholder-red-300 focus:outline-none focus:ring-4 focus:ring-red-400 transition-all duration-300 hover:scale-105">
          <option disabled value="" class="text-red-300">学年を選択</option>
          <option class="text-black">年少</option>
          <option class="text-black">年中</option>
          <option class="text-black">年長</option>
          <option class="text-black">小1</option>
          <option class="text-black">小2</option>
          <option class="text-black">小3</option>
          <option class="text-black">小4</option>
          <option class="text-black">小5</option>
          <option class="text-black">小6</option>
          <option class="text-black">中1</option>
          <option class="text-black">中2</option>
          <option class="text-black">中3</option>
          <option class="text-black">一般女子</option>
        </select>
      </div>

      <!-- 道場 -->
      <div>
        <label class="block mb-2 font-semibold text-red-700">道場</label>
        <input v-model="affiliation" list="dojos" placeholder="道場名を入力"
          class="w-full px-4 py-3 border border-red-400 rounded-md bg-red-700 text-white placeholder-red-300 focus:outline-none focus:ring-4 focus:ring-red-400 transition-all duration-300 hover:scale-105" />
        <datalist id="dojos">
          <option value="筑紫野・本部" />
          <option value="福岡・美和台" />
          <option value="福岡・和白" />
          <option value="福岡・新宮" />
          <option value="大野城・平野" />
          <option value="太宰府・長浦台" />
          <option value="筑紫野・天拝" />
          <option value="田川・猪位金" />
          <option value="大野城・白木原" />
          <option value="筑紫野・筑紫野南" />
          <option value="福岡・城南" />
          <option value="飯塚・筑豊" />
        </datalist>
      </div>
      <!-- 道場 -->
      <div>
        <label class="block mb-2 font-semibold text-red-700">1回戦</label>
        <input v-model="firstRound" list="firstRound" placeholder="パートを選択"
          class="w-full px-4 py-3 border border-red-400 rounded-md bg-red-700 text-white placeholder-red-300 focus:outline-none focus:ring-4 focus:ring-red-400 transition-all duration-300 hover:scale-105" />
        <datalist id="firstRound">
          <option value="男子/初級/Aパート" />
          <option value="男子/初級/Bパート" />
          <option value="男子/初級/Cパート" />
          <option value="男子/初級/Dパート" />
          <option value="男子/初級/Eパート" />
          <option value="男子/初級/Fパート" />
          <option value="男子/初級/Gパート" />
          <option value="男子/初級/Hパート" />
          <option value="男子/初級/Iパート" />
          <option value="男子/中級/Aパート" />
          <option value="男子/中級/Bパート" />
          <option value="男子/中級/Cパート" />
          <option value="男子/中級/Dパート" />
          <option value="男子/上級/Aパート" />
          <option value="男子/上級/Bパート" />
          <option value="男子/上級/Cパート" />
          <option value="男子/上級/Dパート" />
          <option value="女子/初級/Aパート" />
          <option value="女子/初級/Bパート" />
          <option value="女子/初級/Cパート" />
          <option value="女子/中級/Aパート" />
          <option value="女子/中級/Bパート" />
          <option value="女子/中級/Cパート" />
          <option value="女子/上級/Aパート" />
          <option value="女子/上級/Bパート" />
          <option value="一般女子/Aパート" />
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
            <th class="py-4 px-6 text-sm text-red-700">No.</th>
            <th class="py-4 px-6 text-sm text-red-700">選手名</th>
            <th class="py-4 px-6 text-sm text-red-700">段・級</th>
            <th class="py-4 px-6 text-sm text-red-700">学年</th>
            <th class="py-4 px-6 text-sm text-red-700">所属道場</th>
            <th class="py-4 px-6 text-sm text-red-700">1回戦</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in names" :key="index">
            <td class="py-4 px-6 text-sm text-red-700">{{ names.length - index }}</td>
            <td class="py-4 px-6 text-sm text-red-700">{{ item.name }}</td>
            <td class="py-4 px-6 text-sm text-red-700">{{ item.grade }}</td>
            <td class="py-4 px-6 text-sm text-red-700">{{ item.age }}</td>
            <td class="py-4 px-6 text-sm text-red-700">{{ item.affiliation }}</td>
            <td class="py-4 px-6 text-sm text-red-700">{{ item.firstRound }}</td>
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
const affiliation = ref('')
const firstRound = ref('')
const names = ref([])
const isLoading = ref(false)
const error = ref('')

const loadNames = async () => {
  try {
    const res = await axios.get('/api/players')

    if (res.data?.data) {
      const players = Object.values(res.data.data)
      names.value = [] // 一旦クリア

      players.forEach((player) => {
        const firstRoundInfo = player.rounds?.find((r) => r.round === 1)
        const firstRound = firstRoundInfo?.court_code || ""

        names.value.push({
          name: player.name,
          grade: player.grade,
          age: player.age,
          affiliation: player.affiliation,
          firstRound: firstRound
        })
      })

      console.log("Names loaded:", names.value) // デバッグ用ログ
    } else {
      console.warn("登録レスポンスに有効なデータが含まれていません:", res.data)
    }
  } catch (e) {
    alert('名前一覧の読み込みに失敗しました')
    console.error('名前一覧の読み込みエラー:', e)
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
    const res = await axios.post('/api/players', {
      name: name.value.trim()
      , grade: grade.value.trim()
      , age: age.value.trim()
      , affiliation: affiliation.value.trim()
      , court_code: firstRound.value.trim() // 仮の値を設定
    })
    setTimeout(loadNames, 500); // 読込が早すぎるため0.5秒待機
    // テーブルにデータをセット
    if (res.data?.data) {
      const player = res.data.data
      const firstRoundInfo = player.rounds?.find(r => r.round === 1)
      const firstRound = firstRoundInfo?.court_code || ""
      names.value.push({
        name: player.name,
        grade: player.grade,
        age: player.age,
        affiliation: player.affiliation,
        firstRound: firstRound
      })
    } else {
      console.warn("登録レスポンスに有効なデータが含まれていません:", res.data)
    }
    name.value = ''
    grade.value = ''
    age.value = ''
    affiliation.value = ''
    firstRound.value = ''
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
  if (!firstRound.value.trim()) {
    error.value = '1回戦のパートを入力してください'
    return false
  }
  return true
}

onMounted(() => {
  loadNames()
  // setInterval(loadNames, 10000); // 10秒ごとに取得
})
</script>