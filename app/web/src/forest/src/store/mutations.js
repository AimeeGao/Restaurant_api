
export default {
  showMessage: (state, payload) => {
    state.message.display = false
    let defaultData = {
      display: true,
      text: '',
      time: 2500,
      type: 'success', // warn,info,primary,success
      route: ''
    }
    setTimeout(() => {
      state.message = Object.assign(defaultData, payload)
    }, 10)
  },
  hideMessage: state => {
    state.message.text = ''
    state.message.time = 2500
    state.message.display = false
  }
}
