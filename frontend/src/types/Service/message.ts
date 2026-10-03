import { ApiRequest } from "./client";
import type { GetMessagesInfo, MessageResponse, UsersInfo } from "../Payload/Message";


export function messageRequest(
    receiver_id: number,
    content: string,
    image: File
): Promise<MessageResponse> {
    return ApiRequest(`message/user/${receiver_id}`, {
        method: "POST",
        body: JSON.stringify({
            content: content,
            iamge: image
        })
    });
}


export function searchUser(name: string): Promise<UsersInfo> {
    return ApiRequest("message/search", {
        method: "POST",
        body: JSON.stringify({ name: name })
    });
}


export function getMessage(
    receiver_id: number,
    message_id: number | null
): Promise<GetMessagesInfo> {
    return ApiRequest(`message/user/${receiver_id}`, {
        body: JSON.stringify({ message_id: message_id })
    });
}


export function getAllUsers(): Promise<UsersInfo> {
    return ApiRequest("message/available");
}

