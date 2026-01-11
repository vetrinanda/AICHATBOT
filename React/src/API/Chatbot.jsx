import api from "./api";


export const sendMessage = async (prompt) => {
    try {
        const response = await api.post('/chatbot/', { user: prompt });
        return response.data;
    } catch (error) {
        console.error("Error sending message:", error);
        throw error;
    }
};

export default sendMessage;





// export const fetchChatHistory = async () => {
//     try {
//         const response = await api.get('/chatbot/history/');
//         return response.data;
//     } catch (error) {
//         console.error("Error fetching chat history:", error);
//         throw error;
//     }