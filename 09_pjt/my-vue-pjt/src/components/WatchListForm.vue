<template>
  <div class="box">
    <h1>{{msg}}</h1>
    <div>
        <input type="text" v-model.trim="movie" @keyup.enter="inputMovie">
        <button @click="inputMovie">Add</button>
    </div>
  </div>
</template>

<script>
export default {
    name: 'WatchListForm',
    props: {
        msg:String,
    },
    data() {
        return {
            movie:null,
        }
    },
    methods: {
        inputMovie() {
            if (this.movie) {
                this.$store.dispatch('addWatchMovie',this.movie)
            } else {
                alert("입력해")
            }
            this.movie=null
        }
    }
}
</script>

<style>
.box {
    border-radius: 15px;
    background-color: rgb(13, 202, 240, 0.1);
    width: 100%;
    height: 200px;
    display: flex;
    justify-content: center;
    flex-wrap: nowrap;
    flex-direction: column;
    align-items: center;
}
</style>