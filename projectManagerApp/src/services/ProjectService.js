import axios from "axios";

const API_URL = "http://127.0.0.1:5000";

export function getProjects() {
    return axios.get(`${API_URL}/projects`);
}

export function createProject(project) {
    return axios.post(`${API_URL}/projects`, project);
}

export function deleteProject(id) {
    return axios.delete(`${API_URL}/projects/${id}`);
}

export function addMember(projectId, member) {
    return axios.post(`${API_URL}/projects/${projectId}/members`, member);
}

export function removeMember(projectId, memberId) {
    return axios.delete(`${API_URL}/projects/${projectId}/members/${memberId}`);
}
