<template>
  <section class="home-hero">
    <div class="hero-bg"></div>
    <div class="hero-content">
      <h1 class="main-title">武神会</h1>
      <h1 class="sub-title">全日本空手形大会</h1>
      <div class="ranking-section">
        <h2 class="ranking-title">出場選手</h2>
        <div class="category">
          <h3>男子</h3>
          <div class="btn-group">
            <button @click="handleClick('menAdvancedResult')">上級</button>
            <button @click="handleClick('menIntermediateResult')">中級</button>
            <button @click="handleClick('menBeginnerResult')">初級</button>
          </div>
        </div>
        <div class="category">
          <h3>女子</h3>
          <div class="btn-group">
            <button @click="handleClick('womenAdvancedResult')">上級</button>
            <button @click="handleClick('womenIntermediateResult')">中級</button>
            <button @click="handleClick('womenBeginnerResult')">初級</button>
          </div>
        </div>
        <div class="category">
          <h3>一般</h3>
          <div class="btn-group">
            <button @click="handleClick('womensOpenResult')">一般女子</button>
          </div>
        </div>
      </div>
      <div class="ranking-section">
        <h2 class="ranking-title">順位</h2>
        <div class="category">
          <h3>男子</h3>
          <div class="btn-group">
            <button @click="handleClick('menAdvanced')">上級</button>
            <button @click="handleClick('menIntermediate')">中級</button>
            <button @click="handleClick('menBeginner')">初級</button>
          </div>
        </div>
        <div class="category">
          <h3>女子</h3>
          <div class="btn-group">
            <button @click="handleClick('womenAdvanced')">上級</button>
            <button @click="handleClick('womenIntermediate')">中級</button>
            <button @click="handleClick('womenBeginner')">初級</button>
          </div>
        </div>
        <div class="category">
          <h3>一般</h3>
          <div class="btn-group">
            <button @click="handleClick('womensOpen')">一般女子</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const props = defineProps(['onChangePage'])

function handleClick(category) {
  console.log('Selected category:', category)
  // App.vueのページ変更のみを実行
  props.onChangePage(category)
}
</script>