<template>
  <h1>Listado de Mascotas con Vue.js</h1>

  <div class="container">
    <a href="#" type="button" class="btn btn-success">
      Registrar nueva mascota
    </a>

    <div class="row"
      v-if="!!listaMascotas.length"
    >
      <div
        v-for="(mascota, index) in listaMascotas"
        :key="index"
        class="col">
        <CardMascota
          :nombre="mascota.nombre"
          :sexo="mascota.sexo"
          :edad="mascota.edad"
          :fecha_rescate="mascota.fecha_rescate"
          :persona="`${mascota.persona.nombre} ${mascota.persona.apellidos}`"
          :vacunas="mascota.vacunas"
        />
      </div>
    </div>
    <div v-else>
      ¡Ups!... Parece que no hay nada aqui.
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CardMascota from './components/CardMascota.vue'

export default {
  name: 'App',

  components: {
    CardMascota
  },

  data: function () {
    return {
      listaMascotas: [],
    }
  },

  methods: {
    fetchListaMascotas: async function () {
      const response = await axios.get('/api/mascotas/')
      this.listaMascotas = response.data;
    }
  },

  mounted() {
    this.fetchListaMascotas()
  }
}
</script>

<style>
</style>
