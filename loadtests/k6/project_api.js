import http from 'k6/http';
import { check, sleep } from 'k6';
export const options = {
  vus: 20,
  duration: '2m',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<800'],
  },
};
export default function () {
  const params = { headers: { 'x-api-key': __ENV.API_KEY || 'change-me-admin-key' } };
  const res = http.get(`${__ENV.BASE_URL || 'http://localhost:8000'}/v1/catalog`, params);
  check(res, { 'status is 200': (r) => r.status === 200 });
  sleep(1);
}
