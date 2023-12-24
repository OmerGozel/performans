import { configureStore } from '@reduxjs/toolkit'
import denemeReducer from '../features/deneme/denemeSlice'

export const store = configureStore({
  reducer: {
    deneme:denemeReducer,
  },
})