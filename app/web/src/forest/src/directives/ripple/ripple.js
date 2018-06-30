
export default {
  inserted: function(el) {
    // const isMobile = window.navigator.userAgent.match(/Mobile/) && window.navigator.userAgent.match(/Mobile/)[0] === 'Mobile'
    const isMobile = false
    const event = isMobile ? 'touchstart' : 'click'
    el.setAttribute('v-ripple', 'ripple')
    el.addEventListener(event, function (e) {
      // e.preventDefault()
      let button = el
      let rect = button.getBoundingClientRect()
      let btnWidth = rect.width
      let posMouseX = 0
      let posMouseY = 0

      if (isMobile) {
        posMouseX = e.changedTouches[0].pageX - rect.left
        posMouseY = e.changedTouches[0].pageY - rect.top
      } else {
        posMouseX = e.x - rect.left
        posMouseY = e.y - rect.top
      }

      let baseCSS = `
        position: absolute; width: ${btnWidth * 2}px; height: ${btnWidth * 2}px; transition: all linear 1000ms; 
        transition-timing-function:cubic-bezier(0.250, 0.460, 0.450, 0.940);border-radius: 50%; 
        background: var(--color-ripple); top:${posMouseY - btnWidth}px; left:${posMouseX - btnWidth}px; 
        pointer-events: none; transform:scale(0)`

      var rippleEffect = document.createElement('span')
      rippleEffect.style.cssText = baseCSS

      el.style.overflow = 'hidden'
      this.appendChild(rippleEffect)

      setTimeout(function() {
        rippleEffect.style.cssText = baseCSS + `transform:scale(1); opacity: 0;`
      }, 5)

      setTimeout(function() {
        rippleEffect.remove()
      }, 1000)
    })
  }
}
