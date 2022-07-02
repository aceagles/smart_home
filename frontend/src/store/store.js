import { configureStore } from '@reduxjs/toolkit'
import switchesReducer from './switches/switchSlice'

export default configureStore({
    reducer: {
        switches: switchesReducer
    }
})