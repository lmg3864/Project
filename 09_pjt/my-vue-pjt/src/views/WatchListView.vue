<template>
  <div>
    <WatchListForm msg="보고싶은영화"/>
    <WatchListItem v-for="watch in watchlist" :key="watch.id" :watch='watch'/>
  </div>
</template>

<script>
import WatchListForm from '../components/WatchListForm.vue'
import WatchListItem from '../components/WatchListItem.vue'

export default {
    name: 'WatchListView',
    components: {
        WatchListForm,
        WatchListItem
    },
    computed: {
        watchlist() {
            return this.$store.state.watchList
        }
    }
}
</script>

<style>

</style>