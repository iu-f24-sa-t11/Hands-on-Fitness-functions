import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'http://localhost/api',
});

export const getAllMessages = () => {
    return axiosInstance.get(`/messages/`);
};
