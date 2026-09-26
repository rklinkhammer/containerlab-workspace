import test from 'node:test';import assert from 'node:assert/strict';import {serializeRuntime} from '../../backend/live/runtime.ts';
test('runtime reads and capture execute serially, queue is bounded and recovers after failure',async()=>{
 let release!:()=>void;const order:number[]=[];const first=serializeRuntime('test',()=>new Promise<void>(r=>{order.push(1);release=r;}));await Promise.resolve();
 const second=serializeRuntime('test',async()=>{order.push(2);throw Error('EXPECTED');});const secondCheck=assert.rejects(second,/EXPECTED/);
 const third=serializeRuntime('test',async()=>order.push(3));const fourth=serializeRuntime('test',async()=>order.push(4));await assert.rejects(serializeRuntime('test',async()=>order.push(5)),/BUSY/);
 assert.deepEqual(order,[1]);release();await Promise.all([first,secondCheck,third,fourth]);assert.deepEqual(order,[1,2,3,4]);assert.equal(await serializeRuntime('test',async()=>42),42);
});
