<template>
  <article class="liquid-glass rounded-2xl p-5 sm:p-6">
    <h4 class="text-xl font-semibold text-white">{{ title }}</h4>
    <p class="mt-2 text-sm text-slate-300">{{ subtitle }}</p>
  </article>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
  subtitle: {
    type: String,
    required: true,
  },
})
</script>
