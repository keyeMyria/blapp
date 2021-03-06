import * as React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import { applyMiddleware, compose, createStore, StoreEnhancer } from 'redux'
import { offline } from '@redux-offline/redux-offline'
import offlineConfig from '@redux-offline/redux-offline/lib/defaults'
import logger from 'redux-logger'
import thunk from 'redux-thunk'

import { AppContainer } from 'blapp/commerce/containers/App'
import reducer from 'blapp/commerce/reducers'

const persistCallback = () => {
  doRender()
  store.subscribe(() => doRender())
}

const offlineConf = {
  ...offlineConfig,
  persistCallback,
}

const store = createStore(
  reducer,
  compose(
    applyMiddleware(thunk),
    offline(offlineConf) as StoreEnhancer,
    applyMiddleware(logger),
  )
)

const placeholderElem = document.getElementById('APP_PLACEHOLDER')
const doRender = () => render(
  <Provider store={store}>
    <AppContainer />
  </Provider>,
  placeholderElem,
)
