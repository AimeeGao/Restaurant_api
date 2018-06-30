import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/home/Home'
import Login from '@/pages/login/Login'
import Register from '@/pages/register/Register'
import ResetPassword from '@/pages/reset_password/reset_password'
import Forget from '@/pages/forget/forget'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        title: '登录'
      }
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
      meta: {
        title: '首页'
      }
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: {
        title: '注册'
      }
    },
    {
      path: '/forget',
      name: 'forget',
      component: Forget,
      meta: {
        title: '忘记密码'
      }
    },
    {
      path: '/reset_password',
      name: 'reset_password',
      component: ResetPassword,
      meta: {
        title: '重置密码'
      }
    }
  ]
})
