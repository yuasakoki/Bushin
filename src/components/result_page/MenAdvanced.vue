<template>
  <div>
    <h1>男子 上級</h1>
  </div>
    <h4>＜試合結果＞</h4>
  <!-- テーブル -->
    <div class="w-full max-w-6xl overflow-x-auto shadow-lg rounded-lg animate-fadeInUp">
      <table class="min-w-full border-collapse table-auto">
        <thead class="border-red-300 font-sawarabi">
          <tr>
            <th class="py-4 px-6 text-left font-semibold text-Black-700">順位</th>
            <th class="py-4 px-6 text-left font-semibold text-Black-700">名前</th>
            <th class="py-4 px-6 text-left font-semibold text-Black-700">階級</th>
            <th class="py-4 px-6 text-left font-semibold text-Black-700">年齢</th>
            <th class="py-4 px-6 text-left font-semibold text-Black-700">性別</th>
            <th class="py-4 px-6 text-left font-semibold text-Black-700">道場</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in names" :key="index" class="border-b border-gray-200 hover:bg-red-50 transition-colors">
            <td class="py-3 px-6 text-sm text-Black-700">{{ index + 1 }}</td>
            <td class="py-3 px-6 text-sm text-Black-700">{{ item.name }}</td>
            <td class="py-3 px-6 text-sm text-Black-700">{{ item.grade }}</td>
            <td class="py-3 px-6 text-sm text-Black-700">{{ item.age }}</td>
            <td class="py-3 px-6 text-sm text-Black-700">{{ item.sex }}</td>
            <td class="py-3 px-6 text-sm text-Black-700">{{ item.affiliation }}</td>
          </tr>
        </tbody>
      </table>
    </div>
</template>
<script setup>
import { ref } from 'vue'
const show = ref(true)
</script>