<!-- ResultView.vue -->
<template>
  <div v-if="category && category !== ''">
    <h1 class="home-hero">{{ title }}</h1>
    <!-- テーブル -->
    <div class="w-full max-w-6xl overflow-x-auto shadow-lg rounded-lg animate-fadeInUp" :class="tableClass">
      <table class="min-w-full border-collapse table-auto">
        <thead :class="theadClass">
          <tr>
            <th class="py-4 px-6 text-left font-semibold" :class="textClass">No.</th>
            <th class="py-4 px-6 text-left font-semibold" :class="textClass">名前</th>
            <th class="py-4 px-6 text-left font-semibold" :class="textClass">階級</th>
            <th class="py-4 px-6 text-left font-semibold" :class="textClass">年齢</th>
            <th class="py-4 px-6 text-left font-semibold" :class="textClass">性別</th>
            <th class="py-4 px-6 text-left font-semibold" :class="textClass">道場</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in names" :key="index"
            class="border-b border-gray-200 hover:bg-red-50 transition-colors">
            <td class="py-3 px-6 text-sm" :class="textClass">{{ index + 1 }}</td>
            <td class="py-3 px-6 text-sm" :class="textClass">{{ item.name }}</td>
            <td class="py-3 px-6 text-sm" :class="textClass">{{ item.grade }}</td>
            <td class="py-3 px-6 text-sm" :class="textClass">{{ item.age }}</td>
            <td class="py-3 px-6 text-sm" :class="textClass">{{ item.gender }}</td>
            <td class="py-3 px-6 text-sm" :class="textClass">{{ item.affiliation }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div v-else>
    <p>カテゴリが指定されていません</p>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

console.log('ResultView page open!!!!!!!!!!!!')

// Props の定義を改善
const props = defineProps({
  category: {
    type: String,
    default: ''
  }
})

// データの初期化
const names = ref([])
const tableClass = ref('bg-white')
const theadClass = ref('bg-gray-50')
const textClass = ref('text-gray-900')

// computed の循環参照を修正
const title = computed(() => {
  console.log('category:', props.category)
  if (props.category === 'menAdvancedResult') return '男子 上級 - 出場選手'
  if (props.category === 'menIntermediateResult') return '男子 中級 - 出場選手'
  if (props.category === 'menBeginnerResult') return '男子 初級 - 出場選手'
  if (props.category === 'womenAdvancedResult') return '女子 上級 - 出場選手'
  if (props.category === 'womenIntermediateResult') return '女子 中級 - 出場選手'
  if (props.category === 'womenBeginnerResult') return '女子 初級 - 出場選手'
  if (props.category === 'womensOpenResult') return '一般女子 - 出場選手'
  return '普及までお待ちください'
})

// データ取得の例（必要に応じて実装）
const fetchData = async () => {
  try {
    // サンプルデータ（実際のAPIエンドポイントに置き換えてください）
    names.value = [
      { name: '田中太郎', grade: '初段', age: 25, gender: '男', affiliation: '○○道場' },
      { name: '佐藤花子', grade: '二段', age: 30, gender: '女', affiliation: '△△道場' }
    ]
  } catch (error) {
    console.error('データの取得に失敗しました:', error)
  }
}

onMounted(() => {
  if (props.category) {
    fetchData()
  }
})
</script>