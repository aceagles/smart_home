import { createSlice } from "@reduxjs/toolkit";

const switchesSlice = createSlice({
    name: 'switches',
    initialState: {
        switches: []
    },
    reducers: {
        setSwitches: (state, action) => {
            state.switches = action.payload
        },
    }
})

export const {setSwitches} = switchesSlice.actions

export default switchesSlice.reducer