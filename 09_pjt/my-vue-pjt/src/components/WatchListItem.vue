<template>
  <div>
    <h2 @click="watchClick" :class="{'watched' : watch.is_watched}">{{watch.title}}</h2>
  </div>
</template>

<script>
export default {
    name: 'WatchListItem',
    props: {
        watch:Object,
    },
    methods: {
        watchClick() {
            this.$store.dispatch('watchCompleted',this.watch)
        }
    }
}
</script>

<style scoped>
.watched {
    text-decoration: line-through;
    color:gray;
}

div {
    background-color: #f8f9fa;
}
</style>