import {create} from "zustand"

const useUserStore = create((set) => ({
    user : null,
    setUseUser : (data:any) => set((state:any) => ({
        user : data
    }))
}))

export default useUserStore