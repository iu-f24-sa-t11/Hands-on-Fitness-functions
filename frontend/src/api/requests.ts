import axios from 'axios';
import { domain } from "../config.ts"

const axiosInstance = axios.create({
    baseURL: "https://" + domain + "/api",
});

export const getAllMessages = () => {
    return axiosInstance.get(`/messages/`);
};
