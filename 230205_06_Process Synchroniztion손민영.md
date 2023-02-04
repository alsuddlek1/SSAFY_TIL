# Chaper 6. Process Synchroniztion(프로세스 동기화) Concurrency Control(병행 제어)

### 데이터의 접근

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-01-53-10-image.png)

### Race Condition

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-01-53-39-image.png)

### OS에서의 race condition : interrupt handler v.s. kernel

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-01-55-01-image.png)



### OS에서 race condition은 언제 발생하는가?

1. kernel 수행 중 인터럽트 발생 시

2. process가 systen call을 하여 kernel mode로 수행 중인데 context switch가 일어나는 경우

3. Multiprocessor에서 shared memory내의 kernel data



### OS에서의 race condition : interrupt handler v.s. kernel (2)

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-01-55-44-image.png)



### If you preempt CPU while in kernel mode ,,,

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-01-58-20-image.png)



### OS에서의 race condition : interrupt handler v.s. kernel (3)

### ![](230205_06_Process%20Synchroniztion손민영/2023-02-05-01-59-09-image.png)



### Process Synchronization 문제

- 공유 데이터(shared data)의 동시 접근(concurrent acess)은 데이터의 불일치 문제(inconsistency)를 발생시킬 수 있다.

- 일관성(consistency)유지를 위해서는 협력 프로세스(cooperating process)간의 실행 순서(orderly excution)를 정해주는 매커니즘 필요

- Race condition
  
  - 여러 프로세스들이 동시에 공유 데이터를 접근하는 상황
  
  - 데이터의 최종 연산 결과는 마지막에 그 데이터를 다룬 프로세스에 따라 달라짐

- race condition을 막기 위해서는 concurrent process 는 동기화(synchronize)되어야 한다

### Example of a Race Condition

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-02-28-image.png)



### The Critical - Section Problem

- n개의 프로세스가 공유 데이터를 동시에 사용하기를 원하는 경우

- 각 프로세스의 code segment에는 공유 데이터를 접근하는 코드인 critical section이 존재

- Problem
  
  -  하나의 프로세스가 critical section에 있을 대 다른 모든 프로세스는 critical section에 들어갈 수 없어야 한다.

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-03-48-image.png)

### Initial Attempts to Solve Problem

- 두 개의 프로세스가 있다고 가정 P0,P1

- 프로세스들의 일반적인 구조
  
  ![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-04-41-image.png)

- 프로세스들은 수행의 동기화(synchronize)를 위해 몇몇 변수를 공유할 수 있다. => synchronizion varialbe

### 프로그램적 해결법의 충족 조건

- Mutal Exclusion(상호 배제)
  
  - 프로세스 Pi가 critical section 부분을 수행중이면 다른 모든 프로세스들은 그들의 critical section에 들어가면 안된다.

- Progress(진행)
  
  - 아무도 critical section에 있지 않은 상태에서 critical section에 들어가고자 하는 프로세스가 있으면 critical section에 들어가게 해줘야 한다.

- Bounded Waiting(유한 대기)
  
  - 프로세스가 critical section에 들어가려고 요청한 후부터 그 요청이 허용될 때까지 다른 프로세스들이 critical section에 들어가는 횟수에 한계가 있어야 한다.

- 가정
  
  - 모든 프로세스의 수행 속도는 0보다 크다.
  
  - 프로세스들 간의 상대적인 수행 속도는 가정하지 않는다.



### Algorithm 1

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-08-56-image.png)



### Algorithm 2

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-10-12-image.png)

### Algorithm 3(Peterson's Algorithm)

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-11-17-image.png)



### synchronization Hardware

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-12-06-image.png)

### Semaphores

- 앞의 방식들을 추상화시킴

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-13-12-image.png)

### Critical Section of n Processes

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-13-52-image.png)



### Block / Wakeup Implementation

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-14-28-image.png)

### Implementation : block/wakeup version of P() & V()

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-15-18-image.png)



### Which is better?

- Busy-wait v.s. Block/wake up

- Block/wake up overhead vs Critical section 길이
  
  - Critical section의 길이가 긴 경우 Block/Wakeup이 적당
  
  - Critical section의 길이가 매우 짧은 경우 Block/wakeup 오버헤드가 busy-wait 오버헤드보다 더 커질 수 있음
  
  - 일반적으로는 Block/wakeup 방식이 더 좋음

### Two Types of Semaphres

- Counting semaphre
  
  - 도메인이 0 이상인 임의의 정수값
  
  - 주로 resource counting에 사용

- Binary semaphre (=mutex)
  
  - 0 또는 1 값이 가질 수 있는 semaphore
  
  - 주로 mutual exclusion (lock/unlock)에 사용

### Deadlock and Starvation

- Deadlock
  
  - 둘 이상의 프로세스가 서로 상대방에 의해 충족될 수 있는 event를 무한히 기다리는 현상

- S와 Q가 1로 초기화된 semaphore 라 하자.
  
  ![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-19-15-image.png)

- <u>Starvaion</u>
  
  - <mark>indefinite blocking.</mark> 프로세스가 suspend된 이유에 해당하는 세마포어 큐에서 빠져나갈 수 없는 현상

### Dining-Philosophers Problem

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-20-32-image.png)



### Classical Problems of Synchronization

- Bounded-Buffer Problem(Producer - Consumer Problem)

- Readers and Writers Problem

- Dining-Philosophers Problem

### Bounded-Buffer Problem(producer - Consumer Problem)

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-23-11-image.png)

### Bounded-Buffer Problem

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-24-05-image.png)

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-32-37-image.png)

### Readers - Writesrs Problem

- 한 프로세스가 DB에 write 중일 때 다른 process가 접근하면 안됨

- read는 동시에 여럿이 해도 됨

- solution
  
  - writer가 DB에 접근허가를 아직 얻지 못한 상태에서는 모든 대기중인 Reader들을 다 DB에 접근하게 해준다.
  
  - Writer는 대기중인 Reader가 하나도 없을 때 DB 접근이 허용 된다.
  
  - 일단 Writer가 DB에 접근 중이면 Reader 들은  접근이 금지된다
  
  - Writer 가 DB에서 빠져나가야만 Reader의 접근이 허용된다.

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-26-13-image.png)



![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-26-33-image.png)

### dining-Philosophers Problem

- 앞의 soultion의 문제접
  
  - Deadlock 가능성이 있다
  
  - 모든 철학자가 동시에 배가 고파져 왼쪽 젓가락을 집어벌니 경우

- 해결 방안
  
  - 4명의 철학자만이 테이블에 동시에 앉을 수 있도록 한다.
  
  - 젓가락을 두개 모두 집을 수 있을 때에만 젓가락을 집을 수 있게 한다.
  
  - 비대칭
    
    - 짝/홀수 철학자는 왼/오른쪽 젓가락부터 집도록

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-28-45-image.png)

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-29-19-image.png)

### Monitor

- Semaphore의 문제점
  
  - 코딩하기 힘들다
  
  - 정확성(correctness)의 입증이 어렵다
  
  - 자발적 협력(vctuntary cooperation)이 필요하다
  
  - 한번의 실수가 모든 시스템에 치명적 영향

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-30-59-image.png)

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-31-18-image.png)

- 모니터 내에서는 한번에 하나의 프로세스만이 활동 가능

- 프로그래머가 동기화 제약 조건을 명시적으로 코딩할 필요 없음

- 프로세스가 모니터 안에서 기다릴 수 있도록 하기위해 

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-31-54-image.png)

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-32-09-image.png)

![](230205_06_Process%20Synchroniztion손민영/2023-02-05-02-34-03-image.png)
