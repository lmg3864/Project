import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    watchId: 1,
    watchList: [
    ]
  },
  getters: {
  },
  mutations: {
    ADD_WATCH_MOVIE(state,movie) {
      state.watchList.push({id:state.watchId, title:movie, is_watched:false})
      state.watchId += 1
    },
    WATCH_COMPLETED(state,watch) {
      state.watchList = state.watchList.map((e) => {
        if (e.id === watch.id) {
          e.is_watched = !e.is_watched
        }
        return e
      })
    }
  },
  actions: {
    addWatchMovie(context,movie) {
      context.commit('ADD_WATCH_MOVIE',movie)
    },
    watchCompleted(context,watch) {
      context.commit('WATCH_COMPLETED',watch)
    }
  },
  modules: {
  }
})
