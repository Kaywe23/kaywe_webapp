<template>
  <section id="booking" class="px-4 pb-20 sm:px-6 lg:px-8">
    <div class="mx-auto max-w-6xl">
      <div class="liquid-glass rounded-3xl p-6 sm:p-8 lg:p-10">
        <p class="text-xs uppercase tracking-[0.3em] text-blue-200/80">Bookings</p>
        <h3 class="mt-2 text-2xl font-semibold sm:text-3xl">Verfügbar für</h3>
        <ul class="mt-5 grid gap-3 text-sm text-slate-200 sm:grid-cols-2 lg:grid-cols-3">
          <li v-for="item in bookingTypes" :key="item" class="rounded-2xl border border-white/15 bg-white/5 px-4 py-3">
            {{ item }}
          </li>
        </ul>

        <div class="mt-8 grid gap-6 lg:grid-cols-[1fr_1.2fr]">
          <div class="space-y-2 text-sm text-slate-300">
            <p>Für Booking-Anfragen und Kollaborationen:</p>
            <p class="text-white">→ Contact / Booking Formular</p>
            <p>
              oder → Instagram:
              <a href="https://instagram.com/kaywe23" target="_blank" rel="noreferrer" class="font-medium text-blue-200 underline decoration-white/20 underline-offset-4 hover:text-white">
                @kaywe23
              </a>
            </p>
          </div>

          <form class="grid gap-3" @submit.prevent>
            <input class="rounded-xl border border-white/15 bg-black/20 px-4 py-3 text-sm outline-none ring-blue-300/40 placeholder:text-slate-400 focus:ring" type="text" placeholder="Name" />
            <input class="rounded-xl border border-white/15 bg-black/20 px-4 py-3 text-sm outline-none ring-blue-300/40 placeholder:text-slate-400 focus:ring" type="email" placeholder="E-Mail" />
            <textarea class="min-h-28 rounded-xl border border-white/15 bg-black/20 px-4 py-3 text-sm outline-none ring-blue-300/40 placeholder:text-slate-400 focus:ring" placeholder="Event, Datum, Ort, Details"></textarea>
            <button type="submit" class="rounded-xl bg-gradient-to-r from-blue-500 to-violet-500 px-5 py-3 text-sm font-medium text-white transition hover:scale-[1.01]">
              Anfrage senden
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const bookingTypes = ['Club Shows', 'Festivals', 'Private Events', 'Corporate Events', 'Special Electronic Nights']
</script>
