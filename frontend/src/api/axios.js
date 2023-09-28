import axios from "axios"

const instance = axios.create({
    baseURL: "http://localhost:8000/api/v1/shortener"
    // baseURL: "http://172.27.0.2:8000/api/v1/shortener",
})

export default instance