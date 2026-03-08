PromptMachine Test PRD

Product Name: TaskFlow
Type: Web Application
Category: Kanban Task Manager
Purpose: Test PromptMachine’s ability to generate complex frontend architecture with drag-and-drop interactions and state updates.

1. Product Overview
TaskFlow is a lightweight Kanban-style task manager that allows users to organize tasks into different stages of completion.
Users can create tasks and move them between workflow columns using drag-and-drop.

2. Target Users
Primary users: Students managing assignments, Developers tracking tasks, Individuals organizing personal tasks.

3. Core Features
3.1 Kanban Board
The board should contain the following columns: Todo, In Progress, Done.
3.2 Task Cards
Each task card should display: Task title, Short description, Creation time.
Interaction: Click task → open task detail, Drag task → move to another column.
3.3 Create Task
Users should be able to create a new task with Title and Description.
3.4 Drag and Drop
Users can drag a task card between columns.
3.5 Task Details Modal
Clicking a task should open a modal displaying details and options to edit/delete.

4. UI / UX Requirements
Design style: Clean productivity interface, Minimal distractions, Smooth drag animations.

5. Pages / Views
TaskFlow consists of a single-page interface.
Main sections: Top navigation bar, Kanban board area, Task creation modal, Task details modal.

6. Component Architecture (Expected from PromptMachine)
PromptMachine should infer components similar to:
Layout, AppLayout, Navbar, BoardContainer, KanbanBoard, KanbanColumn, TaskCard, CreateTaskModal, TaskDetailModal, Button, InputField, ModalWrapper.

7. State Management
Global state should include: taskList, activeTask, draggedTask, columns.
