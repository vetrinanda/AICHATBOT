import api from "./api";




export const processVideoUrl = async (url, question) => {
    try {
        const response = await api.post('/process-videourl/', { url, question });
        return response.data;
    } catch (error) {
        console.error("Error processing video URL:", error);
        throw error;
    }
};

export default processVideoUrl;