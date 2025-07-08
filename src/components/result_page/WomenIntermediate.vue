<template>
  <div>
    <h1>一般女子</h1>
    <p>出場選手一覧</p>
  </div>
  <div class="womens-open">
    <p>ここに一般女子の試合情報が表示されます。</p>
    <p>選手の登録や試合結果の入力は、管理者メニューから行ってください。</p>
  </div>
  <!-- テーブル -->
    <div class="w-full max-w-6xl mt-16 overflow-x-auto shadow-lg rounded-lg bg-white animate-fadeInUp">
      <table class="min-w-full border-collapse table-auto">
        <thead class="bg-red-100 border-b-2 border-red-300">
          <tr>
            <th class="py-4 px-6 text-left font-semibold text-red-700">No.</th>
            <th class="py-4 px-6 text-left font-semibold text-red-700">名前</th>
            <th class="py-4 px-6 text-left font-semibold text-red-700">階級</th>
            <th class="py-4 px-6 text-left font-semibold text-red-700">年齢</th>
            <th class="py-4 px-6 text-left font-semibold text-red-700">性別</th>
            <th class="py-4 px-6 text-left font-semibold text-red-700">道場</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in names" :key="index" class="border-b border-gray-200 hover:bg-red-50 transition-colors">
            <td class="py-3 px-6 text-sm text-red-700">{{ index + 1 }}</td>
            <td class="py-3 px-6 text-sm text-red-700">{{ item.name }}</td>
            <td class="py-3 px-6 text-sm text-red-700">{{ item.grade }}</td>
            <td class="py-3 px-6 text-sm text-red-700">{{ item.age }}</td>
            <td class="py-3 px-6 text-sm text-red-700">{{ item.sex }}</td>
            <td class="py-3 px-6 text-sm text-red-700">{{ item.affiliation }}</td>
          </tr>
        </tbody>
      </table>
    </div>
</template>
<script setup>
import { ref } from 'vue'
const show = ref(true)
</script>