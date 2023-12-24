import { createSlice } from '@reduxjs/toolkit'

const initialState = [];

export const denemeSlice = createSlice({
  name: 'deneme',
  initialState,
  reducers: {
    add: (state, action) => {
      state.push(action.payload);
    },
    
  },
})

// Action creators are generated for each case reducer function
export const { add } = denemeSlice.actions

export default denemeSlice.reducer